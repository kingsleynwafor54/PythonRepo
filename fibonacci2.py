_cache={}
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n<1:
        raise ValueError("sould be a positive number")
    elif n in _cache:
        return _cache[n]
        raise ValueError("n should be int")
    elif type(n)!=int:
        raise TypeError("n should be int")
    if n in _cache:
        return _cache[n]
    else:
        result= fibonacci(n-1)+fibonacci(n-2)
        _cache[n]=result
        return result

for i in range (1,900):
    print(fibonacci(i))