import sys
input=sys.stdin.readline

def matrixPath(n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            score[i][j]=matrix[i-1][j-1]+max(score[i-1][j],score[i][j-1],score[i-1][j-1])
    return score[n][m]

n,m=map(int,input().split())
matrix=[]
score=[[0 for _ in range(m+1)] for _ in range(n+1)] 

for i in range(n):
    matrix.append([int(m) for m in input().split()])

print(matrixPath(n,m))