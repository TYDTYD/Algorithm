import sys
import heapq
input=sys.stdin.readline
INF=10**12

v,e=map(int,input().split()) 
graph=[[] for _ in range(v)]
Q=[] # 최소 신장 트리에 속하지 않은 정점 리스트
d=[INF]*v # 가중치 갱신 리스트 (모두 무한대로 시작)
visited=[False]*v

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
        w,u=heapq.heappop(h) # 인접 정점 중 가장 가중치가 작은 정점 반환
        if visited[u]:
            continue
        Q.remove(u)
        visited[u]=True
        for i in graph[u]: # 인접 정점 순환하기
            if not visited[i[0]] and i[1]<d[i[0]]: # 가중치가 더 작다면
                d[i[0]]=i[1] # 가중치 갱신
                heapq.heappush(h,(i[1],i[0])) # 우선순위 큐에 입력
    return sum(d) # 최소신장트리의 모든 가중치 반환

print(Prim(graph,0))
