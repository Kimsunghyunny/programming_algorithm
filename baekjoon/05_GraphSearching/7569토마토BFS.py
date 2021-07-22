import sys
from collections import deque
si = sys.stdin.readline

m, n, h = map(int, si().split())
adj = [[list(map(int, si().split())) for _ in range(n)] for _ in range(h)]
# adj[a][b][c] = a높이의 b번 행의 c번째 값

visit = [[[0] * m for _ in range(n)] for _ in range(h)]
dist = [[[-1] * m for _ in range(n)] for _ in range(h)]
dirs = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]

def bfs():
    q = deque()

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if adj[i][j][k] == 1:
                    q.append([i,j,k])
                    visit[i][j][k] = 1
                    dist[i][j][k] = 0

    while q:
        cur = q.popleft()
        #print("cur=",cur[0],"cur[1]=",cur[1],"cur[2]=",cur[2])
        for dh, dn, dm in dirs:
            nh, nn, nm = cur[0] + dh, cur[1] + dn, cur[2] + dm
            #print(nh, nn, nm)
            #print("visit=",visit)
            if nh < 0 or nn < 0 or nm < 0 or nh >= h or nn >= n or nm >= m: continue
            if visit[nh][nn][nm]: continue
            if adj[nh][nn][nm] == -1:continue
            adj[nh][nn][nm] = 1
            q.append([nh,nn,nm])
            visit[nh][nn][nm] = 1
            dist[nh][nn][nm] = dist[cur[0]][cur[1]][cur[2]] + 1
            #print(adj)
bfs()
ans = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if adj[i][j][k] == 0:
                ans = -1

if ans != -1:
    for i in range(h):
        for j in range(n):
            for k in range(m):
                ans = max(ans, dist[i][j][k])

print(ans)
