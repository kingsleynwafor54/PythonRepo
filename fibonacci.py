def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n<1:
        raise ValueError("n should be int")
    elif type(n)!=int:
        raise TypeError("n should be int")
    else:
        return fibonacci(n-1)+fibonacci(n-2)


for i in range (1,900):
    print(fibonacci(i))