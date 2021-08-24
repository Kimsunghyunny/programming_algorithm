import sys
from collections import deque
si = sys.stdin.readline

n, m = map(int, si().split())

arr = [si().strip() for _ in range(n)]

visit = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dirs = [[1,0],[-1,0],[0,1],[0,-1]]

def move(x, y, dx, dy):
    cnt = 0
    while arr[x+dx][y+dy] != '#' and arr[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x,y,cnt

def bfs(rx, ry, bx, by):
    visit[rx][ry][bx][by] = 1
    q = deque()
    q.append([rx,ry,bx,by,1])

    while q:
        rx, ry, bx, by, d = q.popleft()
        if d > 10:
            break
        for dx, dy in dirs:
            nrx, nry, rc = move(rx, ry, dx, dy)
            nbx, nby, bc = move(bx, by, dx, dy)
            if arr[nbx][nby] == 'O':
                continue
            if arr[nrx][nry] == 'O':
                print(d)
                return
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx, nry = nrx - dx, nry - dy
                else:
                    nbx, nby = nbx - dx, nby - dy
            if not visit[nrx][nry][nbx][nby]:
                visit[nrx][nry][nbx][nby] = 1
                q.append([nrx,nry,nbx,nby,d+1])
    print(-1)

#빨간 구슬과 파란 구슬의 위치를 찾기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            rx, ry = i, j
        elif arr[i][j] == 'B':
            bx, by = i, j

bfs(rx,ry,bx,by)