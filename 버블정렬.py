import sys
input=sys.stdin.readline

a=[4,2,5,1,6,9,7,3,8]

def bubbleSort(a):
    switch=0
    for i in range(len(a)-1,-1,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                switch=a[j]
                a[j]=a[j+1]
                a[j+1]=switch
    return a

bubbleSort(a)