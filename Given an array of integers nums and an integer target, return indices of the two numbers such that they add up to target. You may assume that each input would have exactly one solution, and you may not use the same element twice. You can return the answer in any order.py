import sys

data = list(map(int, sys.stdin.read().split()))
target = data[-1]
nums = data[:-1]

seen = {}
for i, x in enumerate(nums):
    if target - x in seen:
        print(seen[target - x], i)
        break
    seen[x] = i
