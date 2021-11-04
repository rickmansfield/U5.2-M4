"""
Currying
In problem solving and functional programming, currying is the practice of simplifying the execution of a function that takes multiple arguments into executing sequential single-argument functions. In simple terms, Currying is used to transform multiple-argument function into single argument function by evaluating incremental nesting of function arguments. Currying also mends one argument to another forms a relative pattern while execution.
[reference](https://www.geeksforgeeks.org/currying-function-in-python/#:~:text=%EE%80%80Currying%EE%80%81%20Function%20%EE%80%80in%20Python%EE%80%81.%20In%20problem%20solving%20and,function%20into%20single%20argument%20function%20by%20evaluating%20)

Tom Tarpy says a function inside a fuction and creating a closer

Memoization
Memoization is a specific type of caching that is used as a software optimization technique. A cache stores the results of an operation for later use.
[Reference Link to Memoization](https://dbader.org/blog/python-memoization#:~:text=In%20this%20article%2C%20I%E2%80%99m%20going%20to%20introduce%20you,the%20results%20of%20an%20operation%20for%20later%20use.)
"""

# simple recursive fib
# [0, 1, 1, 2, 3, 5, 8, 13, 21]
# [0, 1, 1, 2, 3, 5, 8, 13, 21]
# f(n) => f(n - 1) + f(n - 2)


def memo_fib(f):
    cache = {}

    def inner_function(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return inner_function


@memo_fib
def fib_r(n):
    # base case
    if n <= 1:
        return n

    # recursive case
    return fib_r(n - 1) + fib_r(n - 2)


print(fib_r(8))  # => 21
# fib_r(8)
