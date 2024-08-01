0x05. N Queens

Description
The N Queens puzzle is a classic problem in computer science and mathematics. The challenge is to place N non-attacking queens on an N×N chessboard. This project involves writing a Python program to solve the N queens problem using a backtracking algorithm.

Usage
To run the program, use the following command:

bash
Copy code
./0-nqueens.py N
Arguments
N: The size of the chessboard (N×N) and the number of queens to place. It must be an integer greater than or equal to 4.
Output
The program prints every possible solution to the N queens problem. Each solution is printed on a new line in the following format:

bash
Copy code
[[row1, col1], [row2, col2], ..., [rowN, colN]]
where row and col represent the positions of the queens on the chessboard.

Examples
bash
Copy code
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$

Requirements
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7.*)
All your files must be executable
Concepts
Backtracking Algorithms

Recursion
Recursive functions are used to implement backtracking algorithms.

List Manipulations in Python
Creating and manipulating lists is essential to store the positions of queens on the board.

Python Command Line Arguments
Handling command-line arguments with the sys module.

Mock Interview
Practice your algorithmic thinking and optimization techniques by solving the N queens problem. This project not only tests programming and problem-solving skills but also offers an excellent opportunity to learn about algorithmic thinking and optimization techniques.

Author
Project by Oloo Collins


