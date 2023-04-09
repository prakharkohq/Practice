"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
"""
from functools import lru_cache


def fibonacci_number_generate(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci_number_generate(num - 1) + fibonacci_number_generate(num - 2)


memo = {}  # take a dict to remember each value so that you dont have to recall all the time for same value
"""
Memoization or remembering the last solution increases the speed 
"""


def fib_memo(num):
    if num == 0:
        return 0
    if num == 1:
        return 1

    if num - 1 not in memo: memo[num - 1] = fib_memo(num - 1)
    if num - 2 not in memo: memo[num - 2] = fib_memo(num - 2)

    return memo[num - 1] + memo[num - 2]


"""
@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

>>> factorial(10)      # no previously cached result, makes 11 recursive calls
3628800
>>> factorial(5)       # just looks up cached value result
120
>>> factorial(12)      # makes two new recursive calls, the other 10 are cached
479001600
The cache is threadsafe so the wrapped function can be used in multiple threads.
"""


@lru_cache(maxsize=None)
def fib_lru_cache(num):
    if num < 2:
        return num
    return fib_lru_cache(num - 1) + fib_lru_cache(num - 2)


# iterative space-optimized

def fib_iterative(N):
    if N == 0: return 0
    memo = [0, 1]
    for _ in range(2, N + 1):
        memo = [memo[-1], memo[-1] + memo[-2]]

    return memo[-1]


# can use a tuple for better performance
def fib_iterative_tuple(N):
    if N == 0: return 0
    memo = (0, 1)
    for _ in range(2, N + 1):
        memo = (memo[-1], memo[-1] + memo[-2])

    return memo[-1]

# https://en.wikipedia.org/wiki/Fibonacci_sequence#Relation_to_the_golden_ratio
def fib(N):
    golden_ratio = (1 + 5 ** 0.5) / 2
    return int((golden_ratio ** N + 1) / 5 ** 0.5)


if __name__ == "__main__":
    print(fib_lru_cache(100))
