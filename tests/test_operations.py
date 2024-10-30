# -*- coding: utf-8 -*-

"""This module tests the operations module."""

import pytest

from arithmetics.operations import add


def test_add():
    """Test the add function."""
    assert add(1, 2) == 3  # noqa: S101
    assert add(0, 0) == 0  # noqa: S101
    assert add(-1, -1) == -2  # noqa: S101


def test_throw_error_with_bool_input_types_add():
    """Test the add function with bool input types add function."""
    with pytest.raises(TypeError):
        add(1, True)
    with pytest.raises(TypeError):
        add(True, 2)
    with pytest.raises(TypeError):
        add(True, True)
    with pytest.raises(TypeError):
        add(1, False)
    with pytest.raises(TypeError):
        add(False, 2)
    with pytest.raises(TypeError):
        add(False, False)


def test_throw_error_with_wrong_input_types_add():
    """Test the add function with wrong input types add function."""
    with pytest.raises(TypeError):
        add("1", 2)
    with pytest.raises(TypeError):
        add(1, "2")
    with pytest.raises(TypeError):
        add("1", "2")
    with pytest.raises(TypeError):
        add(1.0, 2)
    with pytest.raises(TypeError):
        add(1, 2.0)
    with pytest.raises(TypeError):
        add(1.0, 2.0)
    with pytest.raises(TypeError):
        add(1, [2])
    with pytest.raises(TypeError):
        add([1], 2)
    with pytest.raises(TypeError):
        add([1], [2])
    with pytest.raises(TypeError):
        add(1, (2,))
    with pytest.raises(TypeError):
        add((1,), 2)
    with pytest.raises(TypeError):
        add((1,), (2,))
    with pytest.raises(TypeError):
        add(1, {"2": 2})
    with pytest.raises(TypeError):
        add({"1": 1}, 2)
    with pytest.raises(TypeError):
        add({"1": 1}, {"2": 2})
    with pytest.raises(TypeError):
        add(1, None)
    with pytest.raises(TypeError):
        add(None, 2)
    with pytest.raises(TypeError):
        add(None, None)
    with pytest.raises(TypeError):
        add(1, 2.0)
    with pytest.raises(TypeError):
        add(1.0, 2)
    with pytest.raises(TypeError):
        add(1.0, 2.0)
    with pytest.raises(TypeError):
        add(1, 2.0)
    with pytest.raises(TypeError):
        add(1.0, 2)
    with pytest.raises(TypeError):
        add(1.0, 2.0)
    with pytest.raises(TypeError):
        add(1, 2.0)
    with pytest.raises(TypeError):
        add(1.0, 2)
    with pytest.raises(TypeError):
        add(1.0, 2.0)
