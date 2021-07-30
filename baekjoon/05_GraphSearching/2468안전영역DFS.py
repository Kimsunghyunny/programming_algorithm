import sys
sys.setrecursionlimit(10**9)
si = sys.stdin.readline

n = int(si())
adj = [list(map(int, si().split())) for _ in range(n)]
dirs = [[1,0],[-1,0],[0,1],[0,-1]]

def dfs(x,y,h): # x := 물의 높이
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
        if visit[nx][ny]: continue
        if adj[nx][ny] <= h: continue
        visit[nx][ny] = 1
        dfs(nx,ny,h)

ans = 0
for k in range(max(map(max,adj))):
    visit = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if adj[i][j] > k and visit[i][j] == 0:
                visit[i][j] = 1
                cnt +=1
                dfs(i,j,k)
    ans = max(ans,cnt)

print(ans)
