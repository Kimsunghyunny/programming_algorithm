import sys
si = sys.stdin.readline

n, s = map(int, si().split())
a = list(map(int, si().split()))
cnt = 0

def dfs(idx, sum):
    global cnt

    if idx >= n:
        return
    sum += a[idx]
    if sum == s:
        cnt += 1
    dfs(idx+1,sum-a[idx])
    dfs(idx+1,sum)

dfs(0,0)
print(cnt)