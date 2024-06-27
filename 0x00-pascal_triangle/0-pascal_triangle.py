#!/usr/bin/python3
"""
Pascal's Triangle Module
"""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
    n (int): 
      The number of rows of Pascal's Triangle to generate.

    Returns:
      List[List[int]]: 
         representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of the triangle

    for i in range(1, n):
        row = [1]  # First element of each row is 1
        for j in range(1, i):
            # Sum of the two elements above the current position
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Last element of each row is 1
        triangle.append(row)

    return triangle

def print_triangle(triangle):
    """
    Print Pascal's Triangle.

    Args:
    triangle (List[List[int]]): 
      The Pascal's Triangle to print.
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: ./0-pascal_triangle.py <number_of_rows>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("The number of rows must be an integer.")
        sys.exit(1)

    print_triangle(pascal_triangle(n))
