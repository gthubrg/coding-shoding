n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    a.sort()
    if (a[0]+a[1] == a[-1]):
        print("YES")
    else:
        print("NO")
