import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans = 0

def func(target_idx):
    l, r = 0, n-1
    target = lst[target_idx]
    while l < r:
        if (l == target_idx):
            l += 1
        elif (r == target_idx):
            r -= 1
        else:
            if (lst[l] + lst[r] == target):
                return True
            elif (lst[l] + lst[r] > target):
                r -= 1
            else:
                l += 1
    return False

for x in range(n):
    if func(x):
        ans += 1

print(ans)
