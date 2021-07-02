import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lst = [int(input()) for _ in range(k)]

l, r, ans = 0, 1<<31, 0

def calculate(mid):
    sum = 0
    for x in lst:
        sum += x // mid
    return sum >= n


def binary_search(l, r):
    global ans
    while l <= r:
        mid = (l + r) // 2
        if calculate(mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1


binary_search(l, r)

print(ans)



"""

4 11
802
539
457
743

"""