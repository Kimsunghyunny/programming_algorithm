import sys
from collections import deque
input = sys.stdin.readline

dirs = [[1,0],[-1,0],[1,1],[-1,-1],[0,1],[0,-1],[1,-1],[-1,1]]


def bfs(x,y):
    q = deque()
    q.append((x,y))
    visit[x][y] = 1
    
    while q:
        now = q.popleft()
        for dx, dy in dirs:
            nx, ny = now[0] + dx, now[1] + dy
            if nx < 0 or ny <0 or nx >= h or ny >= w: continue
            if visit[nx][ny]: continue
            if a[nx][ny] == 0: continue
            q.append((nx,ny))
            visit[nx][ny] = 1

while True:
    w,h = map(int ,input().split())
    if w == 0 and h == 0 : break

    visit = [[0]*w for _ in range(h)]
    a = [list(map(int,input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if visit[i][j]: continue
            if a[i][j] == 0: continue
            bfs(i,j)
            cnt +=1
    print(cnt)
            