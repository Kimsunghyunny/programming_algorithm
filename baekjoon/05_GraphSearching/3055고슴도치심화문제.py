import sys
from collections import deque
si = sys.stdin.readline

dirs = [[1,0],[-1,0],[0,1],[0,-1]]

def water_bfs():
    q = deque()
    
    # multisource bfs 구현
    for i in range(r):
        for j in range(c):
            if a[i][j] == '*':
                q.append([i,j])
                visit[i][j] = 1
                distW[i][j] = 0

    while q:
        cur = q.popleft()
        for dx, dy in dirs:
            nx, ny = cur[0] + dx, cur[1] + dy
            if nx < 0 or ny < 0 or nx >= r or ny >= c: continue
            if visit[nx][ny]: continue
            if a[nx][ny] != '.': continue
            q.append([nx,ny])
            visit[nx][ny] = 1
            distW[nx][ny] = distW[cur[0]][cur[1]] + 1

def hedgehog_bfs():
    q = deque()
    visit = [[0]*c for _ in range(r)]

    for i in range(0,r):
        for j in range(0,c):
            if a[i][j] == 'S':
                q.append([i,j])
                distH[i][j] = 0
                visit[i][j] = 1
                break
    
    while q:
        cur = q.popleft()
        print(cur[0],cur[1])
        for dx, dy in dirs:
            nx, ny = cur[0] + dx, cur[1] + dy
            if nx < 0 or ny < 0 or nx >= r or ny >= c: continue
            if visit[nx][ny]: continue
            if a[nx][ny] != '.' and a[nx][ny] != 'D':continue
            print('distW[nx][ny]=',distW[nx][ny],'distH[cur[0][cur[1]]+1=',distH[cur[0]][cur[1]]+1)
            if distW[nx][ny] != -1 and distW[nx][ny] <= (distH[cur[0]][cur[1]]+ 1): continue
            q.append([nx,ny])
            visit[nx][ny] = 1
            distH[nx][ny] = distH[cur[0]][cur[1]] + 1


r, c = map(int, si().split()) # r은 행 c는 열
a = [list(si().strip()) for _ in range(r)]

distW = [[-1]*c for _ in range(r)]
distH = [[-1]*c for _ in range(r)]
visit = [[0]*c for _ in range(r)]
water_bfs()
hedgehog_bfs()

for i in range(r):
    for j in range(c):
        if a[i][j] == 'D':
            if distH[i][j] == -1 :
                print("KAKTUS")
            else:
                print(distH[i][j])
print(distH)