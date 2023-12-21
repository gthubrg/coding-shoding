n = int(input())
a = list(map(int, input().split()))
b, c = 0, 0
for i in range(1, n+1):
    if i % 2 == 0:
        c += max(a[0], a[-1])
        a.remove(max(a[0], a[-1]))
    else:
        b += max(a[0], a[-1])
        a.remove(max(a[0], a[-1]))
print(b, c)
