import sys
from collections import deque
si = sys.stdin.readline


n = int(si())
adj = [list(map(int, si().split())) for _ in range(n)]
dirs = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(x,y,h):
    q = deque()
    q.append(x)
    q.append(y)
    visit[x][y] = 1

    while q:
        tx, ty = q.popleft(), q.popleft()
        for dx, dy in dirs:
            nx, ny = tx + dx, ty + dy
            if nx < 0 or ny <0 or nx >= n or ny>= n: continue
            if visit[nx][ny]: continue
            if adj[nx][ny] <= h: continue
            q.append(nx)
            q.append(ny)
            visit[nx][ny] = 1

ans = 0
for k in range(max(map(max,adj))):
    visit = [[0] * n for _ in range(n)]
    cnt = 0
    for i in  range(n):
        for j in range(n):
            if visit[i][j] == 0 and adj[i][j] > k:
                cnt += 1
                bfs(i,j,k)
    ans = max(ans,cnt)

print(ans)
