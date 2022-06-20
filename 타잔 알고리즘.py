import sys
input=sys.stdin.readline

v=10
visited=[0]*(v+1)
finished=[False]*(v+1)

s=[]
number=0
node=[[] for _ in range(v+1)]
result_SCC=[]
scc=[0 for _ in range(v+1)]

def SCC(start):
    global number
    parent=start
    visited[start]=start
    s.append(start)
    for i in node[start]:
        if not visited[i]:
            parent=min(parent,SCC(i))
        elif not finished[i]:
            parent=min(parent,visited[i])
    
    if parent==start:
        number+=1
        n=s.pop()
        v=[]
        finished[n]=True
        v.append(n)
        scc[n]=number
        while(n!=start):
            n=s.pop()
            finished[n]=True
            v.append(n)
            scc[n]=number
        result_SCC.append(v)

    return parent

node[1].append(2)
node[2].append(3)
node[2].append(4)
node[3].append(1)
node[4].append(5)
node[5].append(6)
node[6].append(7)
node[7].append(8)
node[8].append(5)

SCC(1)
print(scc)
print(result_SCC)
