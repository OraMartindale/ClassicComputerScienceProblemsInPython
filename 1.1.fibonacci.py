
def fib1(n: int) -> int:
    """ Infinite Recursion Example """
    return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    print(fib1(5))
