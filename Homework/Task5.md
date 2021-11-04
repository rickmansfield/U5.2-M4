# Unit 5.2 M4 Task 5

## Instructions
- For a given positive integer n determine if it can be represented as a sum of two Fibonacci numbers (possibly equal).

## Example

- For n = 1, the output should be
```
fibonacciSimpleSum2(n) = true.
```
Explanation: 1 = 0 + 1 = F0 + F1.

- For n = 11, the output should be
```
fibonacciSimpleSum2(n) = true.
```
Explanation: 11 = 3 + 8 = F4 + F6.

- For n = 60, the output should be
```
fibonacciSimpleSum2(n) = true.
```
Explanation: 60 = 5 + 55 = F5 + F10.

- For n = 66, the output should be
```
fibonacciSimpleSum2(n) = false.
```

## Input/Output

- [execution time limit] 4 seconds (py3)

- [input] integer n

- Guaranteed constraints:
```
1 ≤ n ≤ 2 · 109.
```

- [output] boolean
- ```true``` if ```n``` can be represented as ```Fi + Fj```, false otherwise.