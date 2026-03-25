import sys

data = list(map(int, sys.stdin.read().split()))
target = data[-1]
arr = data[:-1]

arr.sort()
n = len(arr)

for i in range(n-2):
    l = i + 1
    r = n - 1
    while l < r:
        s = arr[i] + arr[l] + arr[r]
        if s == target:
            print("true")
            exit()
        elif s < target:
            l += 1
        else:
            r -= 1

print("false")
