import sys
input=sys.stdin.readline

a=[5,3,2,6,8,7,1,9,4]

def insertionSort(a):
    for i in range(1,len(a)):
        loc=i-1
        new=a[i]
        while(loc>=0 and new<a[loc]): # 새로 삽일될 원소의 위치를 찾을때까지
            a[loc+1]=a[loc] # 삽입될 원소를 위해 한칸씩 자리 이동
            loc-=1
        a[loc+1]=new
    return a

insertionSort(a)