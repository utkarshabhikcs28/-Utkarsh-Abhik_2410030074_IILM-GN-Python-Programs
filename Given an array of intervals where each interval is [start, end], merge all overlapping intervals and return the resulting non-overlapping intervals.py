import sys

data = list(map(int, sys.stdin.read().split()))
intervals = [[data[i], data[i+1]] for i in range(0, len(data), 2)]

intervals.sort()

merged = []
for interval in intervals:
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])

for i in merged:
    print(i[0], i[1])
