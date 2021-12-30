import sys
input=sys.stdin.readline

x=[1,2,3,4,5,6,7,8,9,10] # 배열
y=3 # 배열에 존재하는지 찾을 원소

def binary_search(x,y,start,end): # 이분탐색 알고리즘
    if start>end: # 못 찾을 경우 (종료조건)
        return -1 
    mid=(start+end)//2 # 중간값 갱신
    if x[mid]==y:
        return y # 값을 찾을 경우 찾은 값 반환
    elif x[mid]>y:
        return binary_search(x,y,start,mid-1) # 중간값보다 작을 경우 재귀 호출
    elif x[mid]<y:
        return binary_search(x,y,mid+1,end) # 중간값보다 클 경우 재귀 호출
    else:
        return -1

print(binary_search(x,y,0,len(x)-1))