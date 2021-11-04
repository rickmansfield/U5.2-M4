def fibonacciSimpleSum2(n):
        # if 0 is less than n and n is less than 5 then we know we can return
    # true because n will be 1-4 which can be created with 2 fib numbers
    if 0 < n < 5:
        return True

    # first get fibonacci sequence up to n
    seq = [0, 1]
    # starting from 2 and ending at n
    for i in range(2, n):
        # add seq at i - 2 (0 to start) and seq at i - 1 (1 to start)
        fib = seq[i - 2] + seq[i - 1]
        # if n is greater than fib
        if n >= fib:
            # we can append fib to the sequence
            seq.append(fib)
            # if fib is greater than or equal to n we can stop
        else:
            break
    print(seq)