import sys
from collections import deque
si = sys.stdin.readline

n = int(si()) # 사람의 수
goal = list(map(int,si().split()))
case = int(si()) # case 수
adj = [[] for _ in range(n+1)] # 1~n번까지 사람이 있으니깐
visit = [0] * (n+1)
dist = [-1] * (n+1) # 촌수를 저장 (최소 거리 저장)

for _ in range(case):
    x, y = map(int ,si().split())
    adj[x].append(y)
    adj[y].append(x)

def bfs(x):
    global cnt
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

bfs(goal[0])
print(dist[goal[1]])
