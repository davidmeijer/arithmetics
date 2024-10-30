# -*- coding: utf-8 -*-


def add(a: int, b: int) -> str:
    """Add two integers.

    :param a: First integer
    :type a: int
    :param b: Second integer
    :type b: int
    :return: Sum of the two integers
    :rtype: str
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("both arguments must be integers")

    return a + b
