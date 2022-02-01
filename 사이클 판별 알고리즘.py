import sys
input=sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

# 노드의 개수와 간선의 개수 입력 받기
v,e=map(int,input().split())
parent=[0]*(v+1)

for i in range(1,v+1):
    parent[i]=i

Cycle=False # 사이클 발생 여부

for i in range(e):
    a,b=map(int,input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent,a)==find_parent(parent,b):
        Cycle=True
        break
    # 사이클이 발생하지 않았다면 합집합 연산 수행
    else:
        union_parent(parent,a,b)

if Cycle:
    print("사이클이 발생했습니다")
else:
    print("사이클이 발생하지 않았습니다")