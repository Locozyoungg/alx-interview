# Pascal's Triangle

This project implements a function to generate Pascal's Triangle in Python.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Concepts](#concepts)
- [Contributing](#contributing)
- [License](#license)

## Description

The goal of this project is to create a function `pascal_triangle(n)` that returns a list of lists of integers representing the Pascal’s triangle of `n`.

## Installation

No special installation is required. Ensure you have Python 3.x installed on your system.

## Usage

To use the `pascal_triangle` function, simply import it into your Python script or use it in the provided `0-main.py` script.

### Function Definition

```python
def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
    n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
    List[List[int]]: A list of lists of integers representing Pascal's Triangle.
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

