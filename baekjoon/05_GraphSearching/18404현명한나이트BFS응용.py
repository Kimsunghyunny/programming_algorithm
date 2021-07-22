import sys
from collections import deque
si = sys.stdin.readline

n, m = map(int, si().split())
my = list(map(int, si().split()))
enemy = [list(map(int, si().split())) for _ in range(m)]
visit = [[0]*(n+1) for _ in range(n+1)]
dist = [[-1]*(n+1) for _ in range(n+1)]
dirs = [[1,2],[2,1],[1,-2],[2,-1],[-1,2],[-2,1],[-1,-2],[-2,-1]]

def bfs(x, y):
    q = deque()
    q.append([x,y])
    visit[x][y] = 1
    dist[x][y] = 0

    while q:
        cur = q.popleft()
        for dx, dy in dirs:
            nx, ny = cur[0] + dx, cur[1] + dy
            if nx < 0 or ny < 0 or nx > n or ny > n: continue
            if visit[nx][ny]: continue
            q.append([nx,ny])
            visit[nx][ny] = 1
            dist[nx][ny] = dist[cur[0]][cur[1]] + 1

bfs(my[0],my[1])
for x, y in enemy:
    print(dist[x][y], end=' ')