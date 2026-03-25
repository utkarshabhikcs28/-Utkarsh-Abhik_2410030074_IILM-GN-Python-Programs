import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
m = data[1]
a = data[2:2+n]
b = data[2+n:2+n+m]
res = list(set(a) | set(b))
print(*res)
