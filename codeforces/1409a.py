# n = int(input())

# for i in range(n):
#     a, b = map(int, input().split())
#     ans = 0
#     a, b = max(a, b), min(a, b)
#     while a != b:
#         for i in range(10, 0, -1):
#             if a-i >= b:
#                 a -= i
#                 ans += 1
#                 break
#     print(ans)
t = int(input())


def main(a, b):
    # a=13
    # b=42
    x = (b-a)/10
    num_10 = abs(b-a)//10
    num_extra = abs(b-a) % 10
    # print(num_10)
    # print(num_extra)
    if a == b:
        print(0)
        return

    if num_extra == 0:
        ans = num_10
    else:
        ans = num_10+1
    print(ans)


for i in range(t):
    a, b = [int(i) for i in input().split()]
    main(a, b)
