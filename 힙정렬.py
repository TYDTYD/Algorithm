import sys
input=sys.stdin.readline

a=[None,2,5,7,6,3,4,9,8,1]

def buildHeap(a,n):
    for i in range(n//2,0,-1):
        heapify(a,i,n)

def heapify(a,k,n): # a[k]를 루트로 하는 트리를 힙성질을 만족하도록 수선한다
    left=2*k
    right=2*k+1
    switch=0

    if right<=n: # k가 두 자식을 가지는 경우
        if a[left]<a[right]:
            smaller=left
        else:
            smaller=right
    elif left<=n: # k의 왼쪽 자식만 있는 경우
        smaller=left
    else: # k가 리프노드인 경우
        return 

    if a[smaller]<a[k]:
        switch=a[k]
        a[k]=a[smaller]
        a[smaller]=switch
        heapify(a,smaller,n)

def heapSort(a,n): # 힙정렬
    heap=[]
    buildHeap(a,n)
    for i in range(n,0,-1):
        change=a[i]
        a[i]=a[1]
        a[1]=change
        heap.append(a[i])
        heapify(a,1,i-1)
    return heap

print(heapSort(a,len(a)-1))