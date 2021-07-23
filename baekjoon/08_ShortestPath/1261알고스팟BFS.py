import sys
from collections import deque
si = sys.stdin.readline

n, m = map(int, si().split())
a = [list(map(int,si().strip())) for _ in range(m)]
dirs = [[1,0],[-1,0],[0,1],[0,-1]]
visit = [[0] * n for _ in range(m)]
dist = [[-1] * n for _ in range(m)]

def bfs():
    q = deque()
    q.append([0,0])
    dist[0][0] = 0
    visit[0][0] = 1
    
    while q:
        cur = q.popleft()
        for dx, dy in dirs:
            nx, ny = cur[0] + dx, cur[1] + dy
            if nx < 0 or ny < 0 or nx >= m or ny >= n: continue
            if visit[nx][ny]: continue
            if a[nx][ny] == 1: #벽인경우
                q.append([nx,ny])
                dist[nx][ny] = dist[cur[0]][cur[1]] + 1
            else: #벽이 아닌경우
                q.appendleft([nx,ny]) # 벽이 아닌 경우가 있을떄 먼저 실행하도록 큐의 앞으로 추가한다.
                dist[nx][ny] = dist[cur[0]][cur[1]]
            visit[nx][ny] = 1

    print(dist[m-1][n-1])

bfs()