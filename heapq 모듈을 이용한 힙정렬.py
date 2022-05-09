import sys
import heapq # heapq 호출
input=sys.stdin.readline

array=[5,4,3,1,2,6,8,9,7]
heap=[]

for i in array:
    heapq.heappush(heap,i) # heap에 배열 원소 집어 넣기

for i in range(len(array)):
    print(heapq.heappop(heap)) # 차례차례로 최솟값 반환