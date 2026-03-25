import sys

arr = list(map(int, sys.stdin.read().split()))
if arr:
    arr = [arr[-1]] + arr[:-1]
print(*arr)
