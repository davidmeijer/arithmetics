# -*- coding: utf-8 -*-

"""This module tests the version module."""

import re

from arithmetics.version import get_version


def test_correct_version_type():
    """Test the correct version type."""
    assert isinstance(get_version(), str)  # noqa: S101


def test_correct_version_format():
    """Test the correct version format using regex."""
    version = get_version()
    assert re.match(r"^\d+\.\d+\.\d+(-dev)?$", version)  # noqa: S101
