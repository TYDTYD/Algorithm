import sys
input=sys.stdin.readline

n=10
f=[0 for i in range(n+1)]

def fib(n):
    if f[n]!=0:
        return f[n]
    else:
        if n==1 or n==2:
            f[n]=1
        else:
            f[n]=fib(n-1)+fib(n-2)
        return f[n]

fib(n)

print(f)