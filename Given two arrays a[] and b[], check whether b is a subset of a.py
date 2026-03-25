import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
m = data[1]
a = data[2:2+n]
b = data[2+n:2+n+m]

set_a = set(a)

for x in b:
    if x not in set_a:
        print("No")
        break
else:
    print("Yes")
