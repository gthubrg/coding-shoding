n=str(input())
b=0
nums=['4','7']
lucky=[]
for i in range(1,int(n)+1):
    r=0
    for j in str(i):
        if j in nums:
            r=0
        else:
            r=1
            break
    if not r:
        lucky.append(i)
for i in n:
    if i in nums:
        b=0
    else:
        b=1
        break
if b:
    c=0
    for i in lucky:
        if int(n)%i==0:
            c=1
            break
    if c:print("YES")
    else:print("NO")
else:
    print("YES")