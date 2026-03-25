import sys

data = list(map(int, sys.stdin.read().split()))
k = data[-1]
arr = data[:-1]

n = len(arr)
arr.sort()

ans = arr[-1] - arr[0]
small = arr[0] + k
big = arr[-1] - k

if small > big:
    small, big = big, small

for i in range(n - 1):
    subtract = arr[i+1] - k
    add = arr[i] + k

    if subtract >= small or add <= big:
        continue

    if big - add <= subtract - small:
        small = add
    else:
        big = subtract

print(min(ans, big - small))
