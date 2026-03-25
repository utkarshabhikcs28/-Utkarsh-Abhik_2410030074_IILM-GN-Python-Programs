import sys

data = list(map(int, sys.stdin.read().split()))
n1 = data[0]
n2 = data[1]
n3 = data[2]

a = data[3:3+n1]
b = data[3+n1:3+n1+n2]
c = data[3+n1+n2:3+n1+n2+n3]

i = j = k = 0
res = []

while i < n1 and j < n2 and k < n3:
    if a[i] == b[j] == c[k]:
        if not res or res[-1] != a[i]:
            res.append(a[i])
        i += 1
        j += 1
        k += 1
    else:
        m = min(a[i], b[j], c[k])
        if a[i] == m:
            i += 1
        elif b[j] == m:
            j += 1
        else:
            k += 1

if res:
    print(*res)
else:
    print(-1)
