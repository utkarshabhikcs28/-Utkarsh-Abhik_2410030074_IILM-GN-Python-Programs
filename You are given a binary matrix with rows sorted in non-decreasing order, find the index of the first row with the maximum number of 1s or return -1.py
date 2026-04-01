import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
m = data[1]
idx = 2

max_row = -1
j = m - 1

for i in range(n):
    while j >= 0 and data[idx + i*m + j] == 1:
        j -= 1
        max_row = i

print(max_row)
