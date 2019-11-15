def fib(n):
    # fibonachi sequence implemented itertively
    if n in (0,1):
        return n
    
    x = 0
    y = 1
    
    for i in range(1, n):
        temp = y
        y = y + x
        x = temp
        del temp
    
    return y


print(fib(303))
