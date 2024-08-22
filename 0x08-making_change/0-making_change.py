#!/usr/bin/python3
"""
This module provides a function to determine the fewest number of coins
needed to meet a given amount total.
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet the given total.
    
    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The total amount for which you need to find the minimum number of coins.
    
    Returns:
        int: The fewest number of coins needed to meet the total. If the total
             cannot be met by any combination of the coins, returns -1.
    """
    if total <= 0:
        return 0

    # Initialize dp array with infinity, and dp[0] = 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Build up the dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, return -1
    return dp[total] if dp[total] != float('inf') else -1
