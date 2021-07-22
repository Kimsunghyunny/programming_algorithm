import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
m = int(input())

l, r, ans = 0, max(lst), 0

def cal(val):
    sum = 0
    for x in lst:
        if x >= val:
            sum += val
        else:
            sum += x
    return sum <= m


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