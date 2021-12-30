key=[]
left=[]
right=[]

def treeSearch(t,x): # 이진 검색트리 검색
    if t==None or key[t]==x:
        return t
    if x<key[t]:
        return treeSearch(left[t],x)
    else:
        return treeSearch(right[t],x)

def treeInsert(t,x): # 이진 검색트리 삽입
    if t==None:
        key[r]=x
        left[r]=None
        right[r]=None
        return r
    if x<key[t]:
        left[t]=treeInsert(left[t],x)
        return t
    else:
        right[t]=treeInsert(right[t],x)
        return t