"""
metric user tests.
"""

import pytest
import wandb

# TODO: improve tests by mocking some features


def test_feature_single(user_test):
    wandb.use_feature("something")


def test_feature_list(user_test):
    wandb.use_feature("something,another")


def test_feature_version(user_test):
    wandb.use_feature("something:beta")


def test_feature_extra_args(user_test):
    wandb.use_feature("something:beta", "unsupported")


def test_feature_extra_kwargs(user_test):
    wandb.use_feature("something:beta", junk="unsupported")
