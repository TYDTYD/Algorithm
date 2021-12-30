import sys
input=sys.stdin.readline

a=[5,4,2,1,8,6,3,9,7]

def selectionSort(a):
    switch=0
    for i in range(len(a)-1,-1,-1):
        largest=0
        for j in range(1,i+1):
            if a[j]>a[largest]:
                largest=j
        switch=a[largest]
        a[largest]=a[i]
        a[i]=switch
    return a

selectionSort(a)