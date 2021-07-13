import sys
si = sys.stdin.readline
sys.setrecursionlimit(10000)


n = int(si())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, si().split())
    adj[x].append(y)
    adj[y].append(x)
ans = [0] * n

def dfs(x, par):

    for y in adj[x]:
        if y == par: continue
        ans[y-1] = x
        dfs(y,x)

dfs(1,-1)
for i in range(1,n):
    print(ans[i])
