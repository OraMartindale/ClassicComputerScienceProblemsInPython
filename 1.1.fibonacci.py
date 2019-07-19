
def fib1(n):
    """ Infinite Recursion Example """
    return fib1(n - 1) + fib1(n - 2)

def fib2(n):
    if n < 2:
        return n
    return fib2(n - 1) + fib2(n - 2)

if __name__ == '__main__':
    print(fib2(5))
    print(fib2(10))
