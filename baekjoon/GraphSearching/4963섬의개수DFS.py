import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dirs = [[1,0],[-1,0],[1,1],[-1,-1],[0,1],[0,-1],[1,-1],[-1,1]]

def dfs(x,y):
    visit[x][y] = 1
    
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny <0 or nx >= h or ny >= w: continue
        if visit[nx][ny] : continue
        if a[nx][ny] == 0 : continue
        dfs(nx,ny)

while True:
    w,h = map(int ,input().split())
    if w == 0 and h == 0 : break

    visit = [[0]*w for _ in range(h)]
    a = [input().strip() for _ in range(h)]
    print(a)
    print(a[0])
    b = [list(map(int,input().split())) for _ in range(h)]
    print(b)
    print(b[1])

    cnt = 0
    for i in range(h):
        for j in range(w):
            if visit[i][j]: continue
            if a[i][j] == 0: continue
            dfs(i,j)
            cnt +=1
    print(cnt)
            