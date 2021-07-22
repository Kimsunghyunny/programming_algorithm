import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [int(input()) for _ in range(n)]

l, r, ans = 0, 1<<31, 0

def cal(val):
    cnt = 0
    for x in lst:
        cnt += x // val
    return cnt >= m
        

def binary_search(l,r):
    global ans
    while l <= r:
        mid = (l + r) // 2
        if cal(mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

binary_search(l,r)
print(ans)