t=0
while True:
    a=str(t)
    sum=0
    for i in a:
        sum+=int(i)**len(a)
    if sum == t:
        print(t)
    t+=1