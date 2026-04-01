import sys

arr = list(map(int, sys.stdin.read().split()))

for x in arr:
    s = str(x)
    if s != s[::-1]:
        print("false")
        break
else:
    print("true")
