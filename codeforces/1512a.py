x = int(input())
for i in range(x):
    n = int(input())
    f = list(map(int, input().split()))
    l = sorted(f)
    print((f.index(l[-1])+1, f.index(l[0])+1)[l.count(l[0]) == 1])
