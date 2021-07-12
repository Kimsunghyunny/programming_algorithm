import sys
from collections import deque
si = sys.stdin.readline

n, m = map(int, si().split())
ans = 101
minVal = 6000
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, si().split())
    adj[a].append(b)
    adj[b].append(a)

def bfs(x):
    global ans, minVal
    q = deque()
    q.append(x)
    visit[x] = 1
    dist[x] = 0

    while q:
        cur = q.popleft()
        for y in adj[cur]:
            if visit[y]:continue
            q.append(y)
            visit[y] = 1
            dist[y] = dist[cur] + 1

    sumval = 0
    for i in range(1,n+1):
        sumval += dist[i]
    if minVal > sumval:
        minVal = sumval
        ans = x

for i in range(1,n+1):
    visit = [0] * (n+1)
    dist = [-1] * (n+1)
    bfs(i)
print(ans)