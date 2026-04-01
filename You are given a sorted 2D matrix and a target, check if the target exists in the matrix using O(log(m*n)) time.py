import sys

data = list(map(int, sys.stdin.read().split()))
m = data[0]
n = data[1]
target = data[-1]
arr = data[2:-1]

l, r = 0, m*n - 1

while l <= r:
    mid = (l + r) // 2
    val = arr[mid]
    if val == target:
        print("true")
        exit()
    elif val < target:
        l = mid + 1
    else:
        r = mid - 1

print("false")
