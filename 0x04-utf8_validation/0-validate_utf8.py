#!/usr/bin/python3
"""
Module for validating UTF-8 encoding.
"""

def validUTF8(data):
    """
    Validate if a given data set represents a valid UTF-8 encoding.

    Args:
    data (list of int): List of integers representing bytes of data.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    n_bytes = 0

    # Masks for checking the most significant bits of a byte.
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Get the 8 least significant bits of the number.
        byte = num & 0xFF

        if n_bytes == 0:
            # Count the number of leading 1's in the byte.
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask >>= 1

            # 1-byte characters
            if n_bytes == 0:
                continue

            # If n_bytes is more than 4 or 1, then it is not valid UTF-8
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check that the next byte is of the form 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        n_bytes -= 1

    return n_bytes == 0

if __name__ == "__main__":
    data1 = [65]
    print(validUTF8(data1))  # True

    data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data2))  # True

    data3 = [229, 65, 127, 256]
    print(validUTF8(data3))  # False
