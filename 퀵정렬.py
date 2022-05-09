import sys
input=sys.stdin.readline

a=[4,6,2,1,7,9,3,8,5]

def quickSort(a,p,r):
    if p<r:
        q=partition(a,p,r) # 매개변수로 기준점 받기
        quickSort(a,p,q-1) # 기준점 기준으로 왼쪽 부분 정렬
        quickSort(a,q+1,r) # 기준점 기준으로 오른쪽 부분 정렬
    return a

def partition(a,p,r):
    x=a[r] # 정렬 기준점
    start=p-1 # 정렬 시작점
    for i in range(p,r):
        if x>=a[i]: # 기준점보다 작거나 같을 경우
            start+=1
            switch=a[i]
            a[i]=a[start]
            a[start]=switch # 기준점보다 작은 원소들을 앞으로 보내기

    switch=a[r]
    a[r]=a[start+1]
    a[start+1]=switch # 기준점을 본인보다 작은 원소 중 가장 큰 원소 바로 뒤로 보내기
    return start+1 # 기준점 반환

quickSort(a,0,len(a)-1)
