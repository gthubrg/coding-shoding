a=int(input())
c,k="",""
for _ in range(a):
    s=str(input())
    temp=set()
    for i in s:
        temp.add(i)
    charocc=[0]*len(temp)
    for i in range(0,len(temp)):
        for j in s:
            charocc[i] += 1
