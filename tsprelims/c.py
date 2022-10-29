import math
n=int(input())
sum=0
for _ in range(n):
    x=int(input())
    sum+=x
average = sum/2
print(math.floor(average))
print(math.ceil(average))