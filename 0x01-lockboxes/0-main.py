#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

def test_canUnlockAll():
    """
    Function to test the canUnlockAll function with multiple test cases.
    """
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # False

if __name__ == "__main__":
    test_canUnlockAll()
