import sys
si = sys.stdin.readline

n, m = map(int, si().split())
arr = sorted(list(map(int, si().split())))
visit = [0] * n
ans = []

def dfs(d):
    if d == m:
        print(*ans)
        return
    for i in range(n):
        if visit[i]:continue
        visit[i] = 1
        ans.append(arr[i])
        dfs(d+1)
        ans.pop()
        visit[i] = 0

dfs(0)