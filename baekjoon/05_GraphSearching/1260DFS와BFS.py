import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
adj = [[] for _ in range(n+1)]

# 인접리스트
for i in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for i in range(n+1):
    adj[i].sort()

visit = [0] * (n+1)


def dfs(x):
    visit[x] = 1
    print(x,end=' ')
    for y in adj[x]:
        if visit[y] == 1:
            continue
        dfs(y)


def bfs(x):
    visit = [0] * (n+1)
    q = deque()
    q.append(x)
    visit[x] = 1

    while q:
        x = q.popleft()
        print(x,end=' ')
        for y in adj[x]:
            if visit[y] == 1:
                continue
            q.append(y)
            visit[y] = 1


dfs(v)
print()
bfs(v)
