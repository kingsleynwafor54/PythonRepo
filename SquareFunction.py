import time
_cache={}
def factorial(n):
        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif type(n) != int:
            raise TypeError("should be int")
        if n in _cache:
            return _cache[n]
        else:
            result=n * factorial(n - 1)
            _cache[n]=result
            time.sleep(1)
            return result


def factorial_run():
    for i in range (21,0,-1):
        print(factorial(i))



print(factorial_run())
