import sys
from collections import deque
si = sys.stdin.readline

n = int(si())
m = int(si())
visit = [0] * (n+1)
dist = [-1] * (n+1)
adj = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, si().split())
    adj[x].append(y)
    adj[y].append(x)

def bfs(x):
    q = deque()
    q.append(x)
    visit[x] = 1
    dist[x] = 0

    while q:
        now = q.popleft()
        for y in adj[now]:
            if visit[y]:continue
            q.append(y)
            visit[y] = 1
            dist[y] = dist[now] + 1

bfs(1)
ans = 0
for i in range(2,n+1):
    if dist[i] == -1: continue
    if dist[i] > 2: continue
    ans += 1
print(ans)
