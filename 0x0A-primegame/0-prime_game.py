#!/usr/bin/python3
def sieve_of_eratosthenes(max_n):
    """Generates a list of booleans indicating prime status for numbers up to max_n."""
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    p = 2
    while p * p <= max_n:
        if primes[p]:
            for i in range(p * p, max_n + 1, p):
                primes[i] = False
        p += 1
    return primes

def count_primes(n, primes):
    """Returns the number of primes up to n using a precomputed list."""
    return sum(primes[:n + 1])

def isWinner(x, nums):
    """Determines the winner of the prime game."""
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    maria_wins = 0
    ben_wins = 0
    
    # Simulate each round
    for n in nums:
        if n == 1:
            ben_wins += 1
            continue

        prime_count = count_primes(n, primes)
        
        # Maria wins if the count of primes is odd, Ben wins if it's even
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
