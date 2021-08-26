import sys
si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))

def dfs(d):
    if d == n:
        ans.append(sum(abs(lst[i+1]-lst[i]) for i in range(n-1)))
        return
    for i in range(n):
        if visit[i]:continue
        lst.append(arr[i])
        visit[i] = 1
        dfs(d+1)
        lst.pop()
        visit[i] = 0

lst = []
ans = []
visit = [0] * n
dfs(0)
print(max(ans))
