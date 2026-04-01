import sys

data = list(map(int, sys.stdin.read().split()))
x = data[-1]
arr = data[:-1]

n = len(arr)
min_len = n + 1
curr_sum = 0
start = 0

for end in range(n):
    curr_sum += arr[end]
    while curr_sum > x:
        min_len = min(min_len, end - start + 1)
        curr_sum -= arr[start]
        start += 1

if min_len == n + 1:
    print(0)
else:
    print(min_len)
