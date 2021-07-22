
import sys
from collections import deque
si = sys.stdin.readline

n, m = map(int ,si().split())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, w = map(int, si().split())
    g[a].append([b,w])
    g[b].append([a,w])

ans = []
def bfs(start, end):
    dist = [-1] * (n+1)
    visit = [0] * (n+1)
    dist[start] = 0
    visit[start] = 1
    q = deque()
    q.append([start, 0])
    
    while q:
        cur = q.popleft()
        for y, w in g[cur[0]]:
            if visit[y]: continue
            q.append([y,w])
            visit[y] = 1
            dist[y] = dist[cur[0]] + w
    return dist[end]

for _ in range(m):
    start, end = map(int, si().split())
    ans.append(bfs(start, end))

for i in range(m):
    print(ans[i])