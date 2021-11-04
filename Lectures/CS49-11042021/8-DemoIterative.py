# iterative generate fib numbers from 0 to n
"""
Let's make a function that gives us a list of the fib sequence up to a finite number for instance...

input: 10
output: [0, 1, 1, 2, 3, 5, 8]

  the resulting list has fib numbers that go up to 10 or less 
  so we do not hit the next fib number as `13` would exceed `10`

input: 20
output: [0, 1, 1, 2, 3, 5, 8, 13]
  the resulting list has fib numbers that go up to 20 or less 
  so we do not hit the next fib number as `21` would exceed `20`

  create a list called fibs to store our resulting sequence in eg [0, 1]

  get the current fib? look at the fibs last item

  - iterate over the data while the current_fib is less than or equal the n value
    - append the current_fib to fibs
    set the current_fib to fibs at the end of the data + fibs at the end of the data minus 1

  - return fibs


"""


def generate_fibonacci(n):
    fibs = [0, 1]
    current_fib = 1

    while current_fib <= n:
        fibs.append(current_fib)
        current_fib = fibs[-1] + fibs[-2]

    return fibs


print(generate_fibonacci(10))  # => [0, 1, 1, 2, 3, 5, 8]
print(generate_fibonacci(20))  # => [0, 1, 1, 2, 3, 5, 8, 13]
# => [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
print(generate_fibonacci(200))
