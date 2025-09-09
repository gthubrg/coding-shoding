n, m = input().split()
n=int(n)
m=int(m)
for i in range(1,n+1):
    if i%2==0:
        b=(i//2)%2==0
        if b:
            print("#",end="")
        for j in range(m-1):
            print(".",end="")
        if not b:
            print("#",end="")
        print()
    else:
        for j in range(m):
            print("#", end="")
        print()