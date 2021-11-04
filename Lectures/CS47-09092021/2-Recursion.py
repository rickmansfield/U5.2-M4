def n_times_loop(n):
    # start
    while True:
        # base case
        if n <= 0:
            return

        # do stuff
        print(n)

        # decrement
        n -= 1

n = 5
n_times_loop(n)
