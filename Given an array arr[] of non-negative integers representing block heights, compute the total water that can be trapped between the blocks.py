import sys

arr = list(map(int, sys.stdin.read().split()))
n = len(arr)

l, r = 0, n - 1
left_max = right_max = 0
water = 0

while l <= r:
    if arr[l] <= arr[r]:
        if arr[l] >= left_max:
            left_max = arr[l]
        else:
            water += left_max - arr[l]
        l += 1
    else:
        if arr[r] >= right_max:
            right_max = arr[r]
        else:
            water += right_max - arr[r]
        r -= 1

print(water)
