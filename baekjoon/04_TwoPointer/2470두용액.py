import sys
import math
si = sys.stdin.readline

n = int(si())
lst = list(map(int, si().split()))
lst.sort()

l, r = 0, n-1
bestSum = 1<<31
v1, v2 = 0, 0

while l < r:
    sum = lst[l] + lst[r]
    if bestSum > abs(sum):
        v1 = lst[l]
        v2 = lst[r]
        bestSum = abs(sum)

    if sum < 0:
        l += 1
    else:
        r -= 1

print(v1, v2, " ")