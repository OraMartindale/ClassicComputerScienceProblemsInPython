
def fib1(n):
    """ Infinite Recursion Example """
    return fib1(n - 1) + fib1(n - 2)

def fib2(n):
    if n < 2:
        return n
    return fib2(n - 1) + fib2(n - 2)

memoizedData = {0: 0, 1: 1}
def fib3(n):
    if n not in memoizedData:
        memoizedData[n] = fib3(n - 1) + fib3(n - 2)
    return memoizedData[n]

from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(n):
    if n < 2:
        return n
    return fib4(n - 1) + fib4(n - 2)

def fib5(n):
    if n == 0:
        return n
    last = 0
    next = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next

if __name__ == '__main__':
    print(fib5(5))
    print(fib5(50))
