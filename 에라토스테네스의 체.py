import math
import sys
input=sys.stdin.readline

n=int(input())
array=[True for _ in range(n+1)]
number=[]

for i in range(2,int(math.sqrt(n))+1):
    if array[i]==True:
        j=2
        while i*j<=n:
            array[i*j]=False
            j+=1

for i in range(2,len(array)-1):
    if array[i]==True:
        number.append(i)

print(number)