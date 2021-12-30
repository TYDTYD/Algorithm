import sys
input=sys.stdin.readline

a=[3,5,4,1,9,8,6,7,2]

def mergeSort(a,p,r): # p-처음 부분 r-마지막 부분
    if p<r: # p와 r이 똑같아 질때까지 재귀 반복
        q=(p+r)//2
        mergeSort(a,p,q)
        mergeSort(a,q+1,r)
        merge(a,p,q,r)
    return a

def merge(a,p,q,r):
    tmp=[]
    i=p
    j=q+1
    while(i<=q and j<=r): # 각 리스트의 범위를 넘기기 전까지
        if a[i]<=a[j]: # 두 배열의 원소를 대소비교
            tmp.append(a[i]) # 임시 리스트에 삽입
            i+=1
        else:
            tmp.append(a[j]) # 임시 리스트에 삽입
            j+=1
    while(i<=q): # 왼쪽 부분 배열이 남은 경우
        tmp.append(a[i])
        i+=1
    while(j<=r): # 오른쪽 부분 배열이 남은 경우
        tmp.append(a[j])
        j+=1
    i=p
    k=0
    while(i<=r):
        a[i]=tmp[k] # 모든 정렬된 결과를 저장
        i+=1
        k+=1
    return a

mergeSort(a,0,len(a)-1)