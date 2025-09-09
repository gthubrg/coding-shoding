a=0
ls=[]
for _ in range(int(input())):
    n=int(input())
    ls=list(map(int, input()))
    for i in range(n):
        for j in range(n-i-1):
            if ls[j] > ls[j+1]:
                a+=1
                ls[j], ls[j+1] = ls[j+1], ls[j]
    print(a)