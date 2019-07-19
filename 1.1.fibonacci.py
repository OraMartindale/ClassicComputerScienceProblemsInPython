
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

if __name__ == '__main__':
    print(fib3(5))
    print(fib3(50))
