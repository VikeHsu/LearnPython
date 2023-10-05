'''
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
'''
dict1 = {'key1':'data1','key2':'data2'}
print(dict1['key1'])

N = 50

fib_known = {0:0,1:1}

def fib_new(n):
    if n in fib_known:
        return fib_known[n]
    else:
        result = fib_new(n-1)+ fib_new(n-2)
        fib_known[n] = result
        return result

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    # if n > 1:
    return fib(n-1) + fib(n-2)


# test:
print(fib_new(N))

print(fib_new(N+1))

print(fib(N))
