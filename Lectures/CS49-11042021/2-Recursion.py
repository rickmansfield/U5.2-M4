def n_times_recurse(n):
    # base case
    if n <= 0:
        return
    # do something
    print(n)

    # recursive call (decrement)
    n_times_recurse(n - 1)

n = 5
n_times_recurse(n)
