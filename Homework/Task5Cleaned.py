def fibonacciSimpleSum2(n):
    if 0 < n < 5:
        return True
    seq = [0, 1]
    
    for i in range(2, n):
        fib = seq[i - 2] + seq[i - 1]
        if n >= fib:
            seq.append(fib)
        else:
            break
    print(seq)