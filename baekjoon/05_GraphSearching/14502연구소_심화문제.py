import sys
from collections import deque
sys.setrecursionlimit(10000)
si = sys.stdin.readline

n, m = map(int, si().split())
# n = 세로 m = 가로
a = [list(map(int, si().split())) for _ in range(n)]
blank = [(i,j) for i in range(n) for j in range(m) if a[i][j] == 0] # 빈공간인 경우 저장, 벽을 세울 수 있는 위치가 되기도 한다.
ans = 0

dirs = [[1,0],[-1,0],[0,1],[0,-1]]
# 완전탐색을 통해, 벽을 만들 수 있는 경우에 대해서 만들어 주며 dfs로 벽을 3개 만든다.
# 그리고 이후 bfs를 통해 바이러스 위치 기반을 통해 바이러스에 전염된 공간을 찾아 visit처리를 하고, visit처리가 안되어 있는 공간의 max값을 찾아야한다.

def bfs():
    global ans
    visit = [[0]*m for _ in range(n)]
    cnt = 0
    q = deque()
    for i in range(n):
        for j in range(m):
            if a[i][j] == 2:
                q.append(i)
                q.append(j)

    while q:
        x, y = q.popleft(), q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if a[nx][ny] != 0: continue
            if visit[nx][ny]: continue
            visit[nx][ny] = 1
            q.append(nx)
            q.append(ny)

    for i in range(n):
        for j in range(m):
            if visit[i][j]: continue
            if a[i][j] != 0: continue
            cnt += 1
    ans = max(ans, cnt)



def dfs(idx, selectedCnt):
    if selectedCnt == 3:
        bfs()
        return
    if idx == len(blank): # 더이상 세울 수 있는 벽이 없는 경우
        return
    
    a[blank[idx][0]][blank[idx][1]] = 1
    dfs(idx + 1, selectedCnt + 1)

    a[blank[idx][0]][blank[idx][1]] = 0
    dfs(idx + 1, selectedCnt)


dfs(0,0)
print(ans)