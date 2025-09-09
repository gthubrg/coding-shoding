points=[]
nums=[0,0,0]
b=1
sums=[0,0,0]
for _ in range(8):
    x,y,z = map(int, input().split())
    points.append([x,y,z])
for pos in range(3):
    for i in range(0,len(points)):
        if points[i][pos]!=0:
            nums[pos] = points[i][pos]
            break
    for i in range(0,len(points)):
        sums[pos]+=abs(points[i][pos])
for i in range(0,3):
        for j in range(0,len(points)):
            if points[j][i] != 0 and points[j][i] != nums[i]:
                b=0
                break
        if b==0:
            break
for i in range(3):
    if sums[i]%nums[i]!=0:
        b=0
        break
if b != 0:
    print("YES")
    print(((points[len(points)-1][0]-points[0][0]))**2+((points[len(points)-1][1]-points[0][1]))**2+((points[len(points)-1][2]-points[0][2]))**2)
    
else:
    print("NO")