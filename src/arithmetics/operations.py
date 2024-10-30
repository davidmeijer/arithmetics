# -*- coding: utf-8 -*-

"""Module with arithmetic operations."""


def add(a: int, b: int) -> int:
    """Add two integers.

    :param a: First integer
    :type a: int
    :param b: Second integer
    :type b: int
    :return: Sum of the two integers
    :rtype: int
    :raises TypeError: If either a or b is not an integer
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("both arguments must be integers")

    # check if input is a bool
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("both arguments must be integers")

    return a + b
