def n_times_recurse(n):  # T O(n) S O(n)
    # base case
    if n <= 0:
        return

    # do stuff
    print(n)

    # decrement
    n_times_recurse(n - 1)


n = 5
n_times_recurse(n)

# n_times_recurse(5)
# n_times_recurse(4)
# n_times_recurse(3)
# n_times_recurse(2)
# n_times_recurse(1)
# n_times_recurse(0)
