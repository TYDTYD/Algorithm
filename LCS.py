import sys
input=sys.stdin.readline

a=input() # 대조할 문자열 입력
b=input() # 대조할 문자열 입력
C=[] # 저장할 배열

def LCS(m,n,c,d): # m,n은 두 문자열의 길이 c,d는 두 문자열
    for i in range(m):
        C.append([0 for j in range(n)])
    for i in range(1,m):
        for j in range(1,n):
            if c[i-1]==d[j-1]: # 두 문자열이 같다면
                C[i][j]=C[i-1][j-1]+1 # 이전 결과값에 1 증가하여 갱신
            else:
                C[i][j]=max(C[i-1][j],C[i][j-1]) # 같지않다면 이전 결과값 중 큰 값 갱신
    return C[m-1][n-1] # 최장공통부분순서 길이 반환

if len(a)<len(b):
    print(LCS(len(a),len(b),a,b))
else:
    print(LCS(len(b),len(a),b,a))