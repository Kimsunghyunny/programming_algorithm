import sys
si = sys.stdin.readline

n = int(si())
lst = list(map(int, si().split()))
lst.sort()
x = int(si())

l, r = 0, n-1
ans = 0

while l < r:
    sum = lst[l] + lst[r]
    if sum == x:
        ans += 1
        r -= 1
    elif sum < x:
        l += 1
    else:
        r -= 1

print(ans)