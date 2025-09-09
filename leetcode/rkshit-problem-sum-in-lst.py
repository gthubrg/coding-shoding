lst=list(map(int,input().split()))
n=int(input())
temp=[]
for i in range(len(lst)):
    for j in range(len(lst)):
        if i!=j and (lst[i]+lst[j]) == n and j not in temp:
            print(lst[i],lst[j])
            temp.append(i)