def fib(n):
    previous, next = 0, 1
    if n >= 2:
       for i in range(n - 1):
           temp = previous + next
           previous = next
           next = temp 
    else:
        return n
    return next

print(fib(9))