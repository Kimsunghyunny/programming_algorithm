import sys
input = sys.stdin.readline

n, m = map(int,input().split())
lst = list(map(int, input().split()))

l, r, ans = max(lst), 1<<31, 0

def cal(val):
    cnt, sum = 1, 0
    for x in lst:
        if sum + x > val:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt <= m

def binary_search(l,r):
    global ans
    while l <= r:
        mid = (l + r) // 2
        if cal(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1


binary_search(l,r)
print(ans)