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
    res = {}
    def fibonacci(n):
        nonlocal a, b
        if n in res:
            return res[n]
        if n == 1:
            res[n] = 1
        else:
            a, b = b, a + b
            res[n] = b
        return res
    return fibonacci

fibonacci = fibonacci_memo()
start1 = time.time()
for i in range(1, 10):
    print(*fibonacci(i).values())
stop1 = time.time()
print(stop1 - start1)
