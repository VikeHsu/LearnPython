'''
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
'''
dict1 = {'key1':'data1','key2':'data2'}
print(dict1['key1'])

N = input("Type the fib number you want to calculate")

fib_known = {0:0,1:1}

def fib_new(n):
    if n in fib_known:
        return fib_known[n]
    else:
        result = fib_new(n-1)+ fib_new(n-2)
        fib_known[n] = result
        return result

def fib_dp(n):
    a = 0
    b = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return a + b

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    # if n > 1:
    return fib(n-1) + fib(n-2)

# test:
print(fib_dp(N))

print(fib_new(N))

#print(fib(N))
