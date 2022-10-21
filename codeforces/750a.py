a, b = map(int, input().split())
time = 240 - b
ans=0
for i in range(1,a+1):
    if not time >= 5*i:
        break
    time -= 5*i
    ans+=1
print(ans)