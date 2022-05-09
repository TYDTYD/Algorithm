def counting_sort(list,k): # k는 list에서 가장 큰 수보다 더 커야 한다
    count_list=[0]*k # 1부터 k까지 list에 속한 자연수 세는 배열
    sorted_list=[0]*len(list)
    for i in list:
        count_list[i]+=1
    for i in range(1,k):
        count_list[i]+=count_list[i-1]
    for i in range(len(list)):
        sorted_list[count_list[list[i]]-1]=list[i]
        count_list[list[i]]-=1
    return sorted_list

s=[1,4,3,5,3,2,7,2,4,6,9] # s에서 가장 큰 수가 9이므로 k는 10

print(counting_sort(s,10))