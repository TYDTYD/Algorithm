import sys
input=sys.stdin.readline

def getParent(parent,x): # 부모 노드를 찾는 함수
    if parent[x]==x:
        return x
    else:
        return getParent(parent,parent[x])

def unionParent(parent,a,b): # 두 부모를 합치는 함수
    a=getParent(parent,a)
    b=getParent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

def findParent(parent,a,b):
    a=getParent(parent,a)
    b=getParent(parent,b)
    if a==b:
        return 1
    else:
        return 0

parent=[0]
for i in range(1,11):
    parent.append(i)

unionParent(parent,1,2)
unionParent(parent,2,3)
unionParent(parent,3,4)
unionParent(parent,5,6)
unionParent(parent,6,7)
unionParent(parent,7,8)

print(findParent(parent,1,5))
unionParent(parent,2,8)
print(findParent(parent,1,5))