import sys
from collections import deque
si = sys.stdin.readline

n, m = map(int, input().split())
a = [list(si().strip()) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
dist = [[0]*m for _ in range(n)]


def bfs(col, row):
    global dist
    q = deque()
    q.append([col, row])
    visit[col][row] = 1
    dist[col][row] = 1

    while q:
        cur = q.popleft()
        for dx, dy in dirs:
            nx, ny = cur[0] + dx, cur[1] + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visit[nx][ny]:
                continue
            if a[nx][ny] == '0':
                continue
            q.append([nx, ny])
            visit[nx][ny] = 1
            dist[nx][ny] = dist[cur[0]][cur[1]] + 1


bfs(0, 0)
print(dist[n-1][m-1])
