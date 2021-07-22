# 정렬 뒤에 두 포인터를 이용하면 o(nlongN)이 된다.

import sys
input = sys.stdin.readline

n = int(input())
lst = sorted(list(map(int, input().split())))
x = int(input())

l, r, ans = 0, n-1, 0

while l < r:
    sum = lst[l] + lst[r]
    if sum == x:
        ans += 1
        l += 1
    elif sum < x:
        l += 1
    else:
        r -= 1

print(ans)
