import sys

arr = list(map(int, sys.stdin.read().split()))
arr.sort()
n = len(arr)

if n % 2 == 1:
    print(arr[n//2])
else:
    print((arr[n//2 - 1] + arr[n//2]) / 2)
