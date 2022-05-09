import sys
input=sys.stdin.readline

a=[1,7,5,4,8,9,3,2,6]

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


def select(a,p,r,i):
    if p==r:
        return a[p]
    q=partition(a,p,r)
    k=q-p+1
    if i<k:
        return select(a,p,q-1,i)
    elif i==k:
        return a[q]
    else:
        return select(a,q+1,r,i-k)


print(select(a,0,len(a)-1,1))