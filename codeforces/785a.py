models=["Tetrahedron", "Cube", "Octahedron", "Dodecahedron", "Icosahedron"]
sides=[4,6,8,12,20]
n=int(input())
ans=0
for _ in range(n):
    shape=str(input())
    ans+=sides[models.index(shape)]
print(ans)