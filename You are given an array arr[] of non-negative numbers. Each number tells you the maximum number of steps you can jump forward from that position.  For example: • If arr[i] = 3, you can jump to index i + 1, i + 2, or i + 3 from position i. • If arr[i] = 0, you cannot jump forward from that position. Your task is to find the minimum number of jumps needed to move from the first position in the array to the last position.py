import sys

arr = list(map(int, sys.stdin.read().split()))
n = len(arr)

if n <= 1:
    print(0)
elif arr[0] == 0:
    print(-1)
else:
    jumps = 1
    max_reach = arr[0]
    step = arr[0]

    for i in range(1, n):
        if i == n - 1:
            print(jumps)
            break

        max_reach = max(max_reach, i + arr[i])
        step -= 1

        if step == 0:
            jumps += 1
            if i >= max_reach:
                print(-1)
                break
            step = max_reach - i
