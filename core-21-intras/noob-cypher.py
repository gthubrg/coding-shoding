n=int(input())
for _ in range(n):
    a=[]
    b=str(input())
    cc=1
    l=1
    for i in range(1,len(b)+1):
        if i==cc:
            a.append(b[i-1])
            l+=1
            cc+=l
    for i in a:
        print(i,end="")
    print()