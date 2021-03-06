import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline

def dfs(v,visited,stack):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            stack.append(i)
            dfs(i,visited,stack)
    stack.append(v)

def dfsR(v,visited,stack):
    visited[v]=True
    stack.append(v)
    for i in graphR[v]:
        if not visited[i]:
            dfsR(i,visited,stack)

v,e=map(int,input().split())
graph=[[] for _ in range(v+1)]
graphR=[[] for _ in range(v+1)]
visited=[False]*(v+1)
stack=[]

for i in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    graphR[b].append(a)

for i in range(1,v+1):
    if not visited[i]:
        dfs(i,visited,stack)

visited=[False]*(v+1)
answer=[]

while stack:
    scc=[]
    point=stack.pop()
    if not visited[point]:
        dfsR(point,visited,scc)
        answer.append(sorted(scc))

print(len(answer))
for i in range(len(answer)):
    for j in range(len(answer[i])):
        print(answer[i][j],end=' ')