import math
n=int(input())
anslst=[]
ans=0
for i in range(n):
    lenth=input()
    array = (map(int,input().split()))
    for j in range(lenth):
        array[j] = math.gcd(array[j], j)
        ans+=1
        if math.gcd(*array) == 1:
            break
    print(ans)
    #incomplete :/