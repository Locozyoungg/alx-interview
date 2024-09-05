# Prime Game

## Overview

**Prime Game** is a competitive game between two players, Maria and Ben. The game involves removing prime numbers and their multiples from a set of consecutive integers. The objective is to determine the winner of each round based on optimal play, where Maria always goes first.

## Game Rules

1. The game is played in rounds, each with a set of consecutive integers from `1` to `n`, where `n` varies for each round.
2. Maria and Ben take turns choosing a prime number from the set and removing that number and all of its multiples.
3. Maria always plays first, and both players play optimally.
4. A player loses when they cannot make a move.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files are interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should use the PEP 8 style (version 1.7.x)
- All files must be executable

## How to Use

### Function Prototype

```python
def isWinner(x, nums)
