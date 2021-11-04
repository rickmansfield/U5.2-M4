def fibi(n):
    fibs = [0, 1]
    current_fib = 1

    # while current_fib <= n:
    for i in range(n - 1):
        fibs.append(current_fib)
        current_fib = fibs[-1] + fibs[-2]

    return fibs[-1]


fibi(8)
