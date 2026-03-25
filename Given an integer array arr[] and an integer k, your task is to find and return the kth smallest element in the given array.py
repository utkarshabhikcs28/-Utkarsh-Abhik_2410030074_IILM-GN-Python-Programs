import sys

data = list(map(int, sys.stdin.read().split()))
k = data[-1]
arr = data[:-1]
arr.sort()
print(arr[k-1])
