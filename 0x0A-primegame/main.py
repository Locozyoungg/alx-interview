#!/usr/bin/python3
import importlib

# Load the module with a special name
prime_game = importlib.import_module('0-prime_game')

# Use the imported function from the module
print("Winner: {}".format(prime_game.isWinner(5, [2, 5, 1, 4, 3])))
