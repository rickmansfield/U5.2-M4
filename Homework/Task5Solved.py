def fibonacciSimpleSum2(n):
    if 0 < n < 5:
        return True
    series = [0, 1]
    
    for eachIndex in range(2, n):
        fib = series[eachIndex - 2] + series[eachIndex - 1]
        if n >= fib:
            series.append(fib)
        else:
            break
    print("Series", series)
    for eachIndex in range(len(series) - 1):  # O(n^2)
        j = 0
        while (series[eachIndex] + series[j]) != n:
            if j == len(series) - 1:
                break
            else:
                j += 1
        if series[eachIndex] + series[j] == n:
            return True

    return False


print(fibonacciSimpleSum2(5))