import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
m = data[1]
mat = []
idx = 2

for i in range(n):
    mat.append(data[idx:idx+m])
    idx += m

top, bottom = 0, n - 1
left, right = 0, m - 1

res = []

while top <= bottom and left <= right:
    for i in range(left, right + 1):
        res.append(mat[top][i])
    top += 1

    for i in range(top, bottom + 1):
        res.append(mat[i][right])
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            res.append(mat[bottom][i])
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            res.append(mat[i][left])
        left += 1

print(*res)
