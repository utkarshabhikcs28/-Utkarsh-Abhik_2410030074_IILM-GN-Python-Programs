import sys

data = list(map(int, sys.stdin.read().split()))
k = data[-1]
arr = data[:-1]

n = len(arr)
count = sum(1 for x in arr if x <= k)

bad = sum(1 for i in range(count) if arr[i] > k)
ans = bad

for i in range(count, n):
    if arr[i - count] > k:
        bad -= 1
    if arr[i] > k:
        bad += 1
    ans = min(ans, bad)

print(ans)
