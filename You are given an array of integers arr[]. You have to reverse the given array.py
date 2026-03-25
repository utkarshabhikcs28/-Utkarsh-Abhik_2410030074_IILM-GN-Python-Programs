import sys

def reverse_array(arr):
    return arr[::-1]

if __name__ == "__main__":
    arr = list(map(int, sys.stdin.read().split()))
    print(*reverse_array(arr))
