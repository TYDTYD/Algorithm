import math
import sys
input=sys.stdin.readline

m=1
TCD=[[209,43,209],[964,3,964]]


for i in range(len(TCD)):
    interval=TCD[i][1]
    p=False
    count=0
    while(interval<=TCD[i][0] and p==False):
        interference=0
        sum=0
        analysis=0
        count+=1
        for j in range(len(TCD)):
            N=math.floor((interval+TCD[j][2]-TCD[j][1])/TCD[j][0])
            if j<i:
                sum+=math.ceil(interval/TCD[j][2])*TCD[j][1]
                interference+=min(N*TCD[j][1]+min(TCD[j][1],interval+TCD[j][2]-TCD[j][1]-N*TCD[j][0]),interval-TCD[i][1]+1)
        new_interval=sum+TCD[i][1]
        analysis=TCD[i][1]+math.floor((1/m)*interference)
        if(analysis==new_interval):
            p=True
        else:
            interval=new_interval
        if(count<=5):
            print(analysis,new_interval,interference)
    if(p==False):
        print(-1)

print(1)
