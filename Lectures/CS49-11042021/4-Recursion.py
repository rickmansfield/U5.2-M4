def n_times_recurse(n):
    if n <= 0:
        return 0
    else:
        n += n_times_recurse(n - 1)
        return n
    print(n)  # Prints 15 if n is 5

