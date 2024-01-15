package handler

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/segmentio/encoding/json"

	"github.com/wandb/wandb/core/internal/lib/corelib"
	pb "github.com/wandb/wandb/core/internal/wandb_core_go_proto"
)

func (h *Handler) sampleHistory(history *pb.HistoryRecord) {
	var value float32
	if h.sampledHistory == nil {
		h.sampledHistory = make(map[string]*ReservoirSampling[float32])
	}
	for _, item := range history.GetItem() {
		err := json.Unmarshal([]byte(item.ValueJson), &value)
		if err != nil {
			continue
		}
		if _, ok := h.sampledHistory[item.Key]; !ok {
			h.sampledHistory[item.Key] = &ReservoirSampling[float32]{
				k:     48,
				delta: 0.0005,
			}
		}
		h.sampledHistory[item.Key].Add(value)
	}
}

type ActiveHistory struct {
	values map[string]*pb.HistoryItem
	step   int64
	flush  func(*pb.HistoryStep, []*pb.HistoryItem)
}

type ActiveHistoryOptions func(ac *ActiveHistory)

func NewActiveHistory(opts ...ActiveHistoryOptions) *ActiveHistory {
	ah := &ActiveHistory{
		values: make(map[string]*pb.HistoryItem),
	}

	for _, opt := range opts {
		opt(ah)
	}
	return ah
}

func WithFlush(flush func(*pb.HistoryStep, []*pb.HistoryItem)) ActiveHistoryOptions {
	return func(ac *ActiveHistory) {
		ac.flush = flush
	}
}

func WithStep(step int64) ActiveHistoryOptions {
	return func(ac *ActiveHistory) {
		ac.step = step
	}
}

func (ah *ActiveHistory) Clear() {
	clear(ah.values)
}

func (ah *ActiveHistory) UpdateValues(values []*pb.HistoryItem) {
	for _, value := range values {
		ah.values[value.GetKey()] = value
	}
}

func (ah *ActiveHistory) UpdateStep(step int64) {
	ah.step = step
}

func (ah *ActiveHistory) GetStep() *pb.HistoryStep {
	step := &pb.HistoryStep{
		Num: ah.step,
	}
	return step
}

func (ah *ActiveHistory) GetItem(key string) (*pb.HistoryItem, bool) {
	if value, ok := ah.values[key]; ok {
		return value, ok
	}
	return nil, false
}

func (ah *ActiveHistory) GetValues() []*pb.HistoryItem {
	var values []*pb.HistoryItem
	for _, value := range ah.values {
		values = append(values, value)
	}
	return values
}

func (ah *ActiveHistory) Flush() {
	if ah == nil {
		return
	}
	if ah.flush != nil {
		ah.flush(ah.GetStep(), ah.GetValues())
	}
	ah.Clear()
}

// flushHistory flushes a history record. It is responsible for handling the history record internally,
// processing it, and forwarding it to the Writer.
func (h *Handler) flushHistory(history *pb.HistoryRecord) {
	if history.GetItem() == nil {
		return
	}

	// adds internal history items to the history record
	// these items are used for internal bookkeeping and are not sent by the user
	// TODO: add a timestamp field to the history record
	var runTime float64 = 0
	if item, ok := h.activeHistory.GetItem("_timestamp"); ok {
		value := item.GetValueJson()
		val, err := strconv.ParseFloat(value, 64)
		if err != nil {
			h.logger.CaptureError("error parsing timestamp", err)
		} else {
			runTime = val - h.timer.GetStartTimeMicro()
		}
	}
	history.Item = append(history.Item,
		&pb.HistoryItem{Key: "_runtime", ValueJson: fmt.Sprintf("%f", runTime)},
		&pb.HistoryItem{Key: "_step", ValueJson: fmt.Sprintf("%d", history.GetStep().GetNum())},
	)

	// handles all history items. It is responsible for matching current history
	// items with defined metrics, and creating new metrics if needed. It also handles step metric in case
	// it needs to be synced, but not part of the history record.
	// This means that there are metrics defined for this run
	if h.metricHandler != nil {
		for _, item := range history.GetItem() {
			step := h.imputeStepMetric(item)
			// TODO: fix this, we update history while we are iterating over it
			// TODO: handle nested step metrics (e.g. step defined by another step)
			if step != nil {
				history.Item = append(history.Item, step)
			}
		}
	}

	h.sampleHistory(history)

	record := &pb.Record{
		RecordType: &pb.Record_History{History: history},
	}
	h.sendRecord(record)

	// TODO unify with handleSummary
	// TODO add an option to disable summary (this could be quite expensive)
	if h.summaryHandler == nil {
		return
	}
	summary := corelib.ConsolidateSummaryItems(h.summaryHandler.Consolidated, history.GetItem())
	h.summaryHandler.UpdateDelta(summary)
}

// handleHistory handles a history record. This is the main entry point for history records.
// It is responsible for handling the history record internally, processing it,
// and forwarding it to the Writer.
func (h *Handler) handleHistory(history *pb.HistoryRecord) {
	// TODO replace history encoding with a map, this will make it easier to handle history
	h.activeHistory = NewActiveHistory(
		WithStep(history.GetStep().GetNum()),
	)
	h.activeHistory.UpdateValues(history.GetItem())

	h.flushHistory(history)

	h.activeHistory.Flush()
}

// imputeStepMetric imputes a step metric if it needs to be synced, but not part of the history record.
func (h *Handler) imputeStepMetric(item *pb.HistoryItem) *pb.HistoryItem {

	// check if history item matches a defined metric or a glob metric
	metric := h.matchHistoryItemMetric(item)

	key := metric.GetStepMetric()
	// check if step metric is defined and if it needs to be synced
	if !(metric.GetOptions().GetStepSync() && key != "") {
		return nil
	}

	// check if step metric is already in history
	if _, ok := h.activeHistory.GetItem(key); ok {
		return nil
	}

	// we use the summary value of the metric as the algorithm for imputing the step metric
	if value, ok := h.summaryHandler.Consolidated[key]; ok {
		// TODO: add nested key support
		hi := &pb.HistoryItem{
			Key:       key,
			ValueJson: value,
		}
		h.activeHistory.UpdateValues([]*pb.HistoryItem{hi})
		return hi
	}
	return nil
}

// matchHistoryItemMetric matches a history item with a defined metric or creates a new metric if needed.
func (h *Handler) matchHistoryItemMetric(item *pb.HistoryItem) *pb.MetricRecord {

	// ignore internal history items
	if strings.HasPrefix(item.Key, "_") {
		return nil
	}

	// check if history item matches a defined metric exactly, if it does return the metric
	if metric, ok := h.metricHandler.Defined[item.Key]; ok {
		return metric
	}

	// if a new metric was created, we need to handle it
	metric := h.metricHandler.createMatchingGlobMetric(item.Key)
	if metric != nil {
		record := &pb.Record{
			RecordType: &pb.Record_Metric{
				Metric: metric,
			},
			Control: &pb.Control{
				Local: true,
			},
		}
		h.handleMetric(record, metric)
	}
	return metric
}

// handlePartialHistory handles a partial history request. Collects the history items until a full
// history record is received.
func (h *Handler) handlePartialHistory(_ *pb.Record, request *pb.PartialHistoryRequest) {

	// This is the first partial history record we receive
	// for this step, so we need to initialize the history record
	// and step. If the user provided a step in the request,
	// use that, otherwise use 0.
	if h.activeHistory == nil {
		var step int64
		switch {
		case request.Step != nil:
			step = request.Step.Num
		case h.runRecord != nil:
			step = h.runRecord.StartingStep
		default:
			// TODO: this should never happen, but we should handle it
			// gracefully, should we raise an error?
			step = 0
		}

		h.activeHistory = NewActiveHistory(
			WithStep(step),
			WithFlush(
				func(step *pb.HistoryStep, items []*pb.HistoryItem) {
					record := &pb.HistoryRecord{
						Step: step,
						Item: items,
					}
					h.flushHistory(record)
				},
			),
		)
	}

	// The HistoryRecord struct is responsible for tracking data related to
	//	a single step in the history. Users can send multiple partial history
	//	records for a single step. Each partial history record contains a
	//	step number, a flush flag, and a list of history items.
	//
	// The step number indicates the step number for the history record. The
	// flush flag determines whether the history record should be flushed
	// after processing the request. The history items are appended to the
	// existing history record.
	//
	// The following logic is used to process the request:
	//
	// -  If the request includes a step number and the step number is greater
	//		than the current step number, the current history record is flushed
	//		and a new history record is created.
	// - If the step number in the request is less than the current step number,
	//		we ignore the request and log a warning.
	// 		NOTE: the server requires the steps of the history records
	// 		to be monotonically increasing.
	// -  If the step number in the request matches the current step number, the
	//		history items are appended to the current history record.
	//
	// - If the request has a flush flag, another flush might occur after for the
	// current history record after processing the request.
	//
	// - If the request doesn't have a step, and doesn't have a flush flag, this is
	//	equivalent to step being equal to the current step number and a flush flag
	//	being set to true.
	if request.GetStep() != nil {
		step := request.Step.GetNum()
		current := h.activeHistory.GetStep().Num
		if step > current {
			h.activeHistory.Flush()
			h.activeHistory.UpdateStep(step)
		} else if step < current {
			h.logger.CaptureWarn("received history record for a step that has already been received",
				"received", step, "current", current)
			return
		}
	}

	// Append the history items from the request to the current history record.
	h.activeHistory.UpdateValues(request.Item)

	// Flush the history record and start to collect a new one with
	// the next step number.
	if (request.Step == nil && request.Action == nil) || (request.Action != nil && request.Action.Flush) {
		h.activeHistory.Flush()
		step := h.activeHistory.GetStep().Num + 1
		h.activeHistory.UpdateStep(step)
	}
}

func (h *Handler) handleSampledHistory(record *pb.Record, response *pb.Response) {
	if h.sampledHistory == nil {
		return
	}
	var items []*pb.SampledHistoryItem

	for key, sampler := range h.sampledHistory {
		values := sampler.GetSample()
		item := &pb.SampledHistoryItem{
			Key:         key,
			ValuesFloat: values,
		}
		items = append(items, item)
	}

	response.ResponseType = &pb.Response_SampledHistoryResponse{
		SampledHistoryResponse: &pb.SampledHistoryResponse{
			Item: items,
		},
	}
}
