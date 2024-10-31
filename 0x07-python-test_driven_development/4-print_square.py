#!/usr/bin/env python3


def print_square(size):
    """
    Prints a square of size `size` with the character `#`.

    Args:
        size (int): The length of the square's sides.

    Raises:
        TypeError: If size is not an integer or if size is a float less than 0.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):  # Check if size is an integer
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")

    if size < 0:  # Check if size is negative
        raise ValueError("size must be >= 0")

    for _ in range(size):  # Loop to print the square
        print('#' * size)


if __name__ == "__main__":
    print_square(3)
