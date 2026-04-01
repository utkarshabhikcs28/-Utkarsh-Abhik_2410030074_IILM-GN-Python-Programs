import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
m = data[1]
mat = []
idx = 2

for i in range(n):
    mat.extend(data[idx:idx+m])
    idx += m

mat.sort()
print(mat[(n*m)//2])
