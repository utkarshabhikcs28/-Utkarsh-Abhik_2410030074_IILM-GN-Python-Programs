import sys

data = list(map(int, sys.stdin.read().split()))
m = data[-1]
arr = data[:-1]

n = len(arr)
if m > n:
    print(-1)
    exit()

arr.sort()
res = float('inf')

for i in range(n - m + 1):
    res = min(res, arr[i + m - 1] - arr[i])

print(res)
