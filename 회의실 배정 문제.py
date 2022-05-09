import sys
input=sys.stdin.readline

s=[(4,1),(3,1),(5,7)] # 회의시간 (종료시간,시작시간)

def Greedy_Schedule(s,n):
    T=[0] # 제일 일찍 끝나는 회의 추가
    last=0
    for i in range(1,n):
        if s[i][1]>=s[last][0]:
            T.append(i)
            last=i
    return len(T) # 회의 할 수 있는 개수 반환

Greedy_Schedule(sorted(s),len(s))