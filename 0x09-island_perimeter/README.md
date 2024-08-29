# Island Perimeter

This project involves creating a Python function that calculates the perimeter of an island represented in a 2D grid. The task tests your understanding of 2D arrays, conditional logic, and algorithmic problem-solving.

## Project Overview

The objective is to create a function `island_perimeter(grid)` that returns the perimeter of the island described in the grid. The grid is a list of lists of integers where:
- `0` represents water.
- `1` represents land.
- Each cell is a square with a side length of 1.
- Cells are connected horizontally or vertically, not diagonally.
- The grid is completely surrounded by water.
- There is only one island, and the island does not contain lakes (water inside that isn’t connected to the water surrounding the island).

## Requirements

- All code will be interpreted on Ubuntu 20.04 LTS using Python 3.4.3.
- Adhere to PEP 8 style guidelines.
- Do not import any external modules.
- All files must be executable.
- The first line of the Python file must be `#!/usr/bin/python3`.
- A `README.md` file at the root of the project is mandatory.

## Function Prototype

```python
def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    :param grid: List of lists of integers representing the grid.
    :return: Integer representing the perimeter of the island.
    """

How the Function Works
Iteration: The function uses nested loops to iterate through each cell of the grid.
Condition Check: For each land cell (1), it checks adjacent cells (top, bottom, left, right).
Perimeter Contribution: If an adjacent cell is water (0) or out of bounds, it contributes to the island's perimeter.
Example
Given the following grid:

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

Calling island_perimeter(grid) will return 12, representing the total perimeter of the island.

Usage
Clone the repository and navigate to the project directory.
Ensure the function file is executable (chmod +x 0-island_perimeter.py).
Import and call the function with your grid data in a Python script or interactive shell.
Additional Notes
The function does not handle grids with multiple islands or lakes inside the island; it is designed for a single island surrounded by water.
Edge cases, such as land cells on the grid's border, are handled within the perimeter calculations.
License
This project is licensed under the MIT License - see the LICENSE file for details.


This README provides a comprehensive overview of the project, detailing the requirements, function implementation, and usage instructions. Let me know if you need any adjustments!

