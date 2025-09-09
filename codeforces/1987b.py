l = int(input())
for _ in range(l):
    r = input()
    a = [int(i) for i in input().split()]
    d = []
    f = []
    n = 0

    for i in range(0, len(a)-1):
        if a[i] > a[i+1] and i+1 not in f:
            #print([a[i], a[i+1], d, f, n])
            for j in range(i+1, len(a)):
                if a[i] > a[j]:
                    d.append(a[i]-a[j])
                    n += 1
                    f.append(j)
                    # print([a[i], a[i+1],d,f,n])
                else:
                    break
    d = list(set(d))
    d.sort()
    d = [0,]+d
    c = 0
    for i in range(0, len(d)-1):
        c += (d[i+1]-d[i])*(n+1)
        n -= 1
    print(c)

# (33×7)+[(248−33)×6]+[(284−248)×5]+[(285−284)×4]+[(307−285)×3]+[(332−307)×2]
