import sys

data = list(map(int, sys.stdin.read().split()))
target = data[-1]
arr = data[:-1]

l, r = 0, len(arr) - 1
ans = len(arr)

while l <= r:
    mid = (l + r) // 2
    if arr[mid] == target:
        print(mid)
        exit()
    elif arr[mid] < target:
        l = mid + 1
    else:
        ans = mid
        r = mid - 1

print(ans)
