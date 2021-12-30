import sys
input=sys.stdin.readline

n=30 # n이 30이상부터 시간이 오래 걸리기 시작함

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(n))