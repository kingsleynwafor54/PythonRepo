def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    elif type(n)!=int:
        raise TypeError("should be int")
    else:
        return n*factorial(n-1)

for i in range (1,900):
    print(factorial(i))
