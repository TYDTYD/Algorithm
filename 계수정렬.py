def counting_sort(list,k):
    count_list=[0]*k
    sorted_list=[0]*len(list)
    for i in list:
        count_list[i]+=1
    for i in range(1,k):
        count_list[i]+=count_list[i-1]
    for i in range(len(list)):
        sorted_list[count_list[list[i]]-1]=list[i]
        count_list[list[i]]-=1
    return sorted_list

s=[1,4,3,5,13,2,7,2,4,6,19]

print(counting_sort(s,20))