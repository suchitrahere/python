# Fibonacci series to print the fibonacci value of the nth position given by user
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        x = 1 
        y = 1
        sum = x + y
        for p in range(3, n):
            x = y
            y = sum
            sum = x + y
        return sum

print(fibonacci(6))
