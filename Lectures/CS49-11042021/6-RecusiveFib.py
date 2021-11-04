# simple recursive fib
# [0, 1, 1, 2, 3, 5, 8, 13, 21]
# [0, 1, 1, 2, 3, 5, 8, 13, 21]
# f(n) => f(n - 1) + f(n - 2)
def fib_r(n):
    # base case
    if n <= 1:
        return n

    # recursive case
    return fib_r(n - 1) + fib_r(n - 2)


print(fib_r(8))  # => 21
# fib_r(8)
