import sys
import heapq
input=sys.stdin.readline
INF=10**12

v,e=map(int,input().split()) 
graph=[[] for _ in range(v)]
Q=[] # 최소 신장 트리에 속하지 않은 정점 리스트
d=[INF]*v # 가중치 갱신 리스트 (모두 무한대로 시작)

for i in range(v):
    Q.append(i) # 모든 정점 입력

for i in range(e):
    a,b,c=map(int,input().split())
    graph[a-1].append((b-1,c))
    graph[b-1].append((a-1,c))

def Prim(graph,start):
    d[start]=0 # 첫 시작 가중치 0으로 갱신
    h=[]
    heapq.heappush(h,(0,start)) # 우선순위 큐에 시작점 입력
    while Q:
        u=deleteMin(h) # 인접 정점 중 가장 가중치가 작은 정점 반환
        for i in graph[u]: # 인접 정점 순환하기
            if i[0] in Q and i[1]<d[i[0]]: # 가중치가 더 작다면
                d[i[0]]=i[1] # 가중치 갱신
                heapq.heappush(h,(i[1],i[0])) # 우선순위 큐에 입력
    return sum(d) # 최소신장트리의 모든 가중치 반환

def deleteMin(heap):
    m=heapq.heappop(heap) # 가중치 가장 작은 정점 반환
    while(m[1] not in Q): # Q에 없는 정점을 반환할 경우(갱신당해 제외된 값이 남았을 경우)
        m=heapq.heappop(heap) # Q에 값이 있을때까지 제거
    Q.remove(m[1]) # 최소 신장 트리에 들어갈 정점 제거
    return m[1]

print(Prim(graph,0))