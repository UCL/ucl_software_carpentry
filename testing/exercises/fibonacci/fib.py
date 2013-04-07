def fib(n):
    # sequence and you shall find
    if n < 0 or int(n) != n:
        return NotImplemented
    elif n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)