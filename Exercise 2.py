import time

def fibonacci_rec(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

start = time.time()
for i in range(1, 10):
    print(fibonacci_rec(i))
stop = time.time()
print(stop - start, '\n')


def fibonacci_memo():
    a, b = 0, 1
    def fibonacci():
        nonlocal a, b
        a, b = b, a + b
        return b
    return fibonacci


start1 = time.time()
fibonacci = fibonacci_memo()
for i in range(1, 10):
    my_fibo = fibonacci()
    print(my_fibo)
stop1 = time.time()
print(stop1 - start1)