n=int(input())
names=[]
for _ in range(n):
    names.append(str(input()))
for i in range(len(names)):
    if i==len(names)-1:
        a=list(names)
    else:
        a=list(names[0:i+1])
    if a.count(names[i])>1:
        print(names[i]+str(a.count(names[i])-1))
    else:
        print("OK")