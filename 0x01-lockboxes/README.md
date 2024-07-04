# Lockboxes Project

## Description
This project involves developing a solution to determine if all boxes in a given list of lists can be opened. Each box is numbered sequentially from 0 to n - 1 and may contain keys to other boxes. The goal is to implement a function that determines if all boxes can be opened.

## Requirements
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Your code should be documented
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable

## Concepts and Resources
To successfully complete this project, you should have a good understanding of the following concepts:
- Lists and List Manipulation
  - [Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- Graph Theory Basics
  - [Graph Theory (Khan Academy)](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:graph-theory)
- Algorithmic Complexity
  - [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/)
- Recursion
  - [Recursion in Python (Real Python)](https://realpython.com/python-thinking-recursively/)
- Queue and Stack
  - [Python Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/queue-in-python/)
- Set Operations
  - [Python Sets (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html#sets)

## File Structure
The project contains the following files:
- `0-lockboxes.py`: Contains the implementation of the `canUnlockAll` function.
- `main_0.py`: Contains the test cases for the `canUnlockAll` function.
- `README.md`: The readme file you are currently reading.

## Implementation
The `canUnlockAll` function determines if all boxes can be opened by using a Depth-First Search (DFS) approach. It uses a stack to manage the boxes to be processed and a set to keep track of opened boxes.

### Usage
1. Ensure both `0-lockboxes.py` and `main_0.py` files are in the same directory.
2. Make both files executable by running:
   ```sh
   chmod +x 0-lockboxes.py
   chmod +x main_0.py

