a=int(input())
ls=list(input().split())
o=0
ans=0
for i in range(0,a):
    b=int(ls[i])
    if b > 0:
        o+=b
    elif b < 0 and o==0:
        ans+=b
    else:
        o-=1
print(ans*-1)