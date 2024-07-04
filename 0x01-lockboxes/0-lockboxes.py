#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
    boxes (list of lists): A list where each index contains a list of keys.

    Returns:
    bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    opened = set()
    stack = [0]
    
    while stack:
        current_box = stack.pop()
        if current_box not in opened:
            opened.add(current_box)
            for key in boxes[current_box]:
                if key < n:
                    stack.append(key)
    
    return len(opened) == n

