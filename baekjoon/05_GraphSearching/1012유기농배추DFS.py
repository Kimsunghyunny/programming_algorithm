import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

t = int(input())
dirs = [[1,0],[-1,0],[0,1],[0,-1]]
ans = []

def dfs(x,y):
    visit[x][y] = 1
    
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny <0 or nx >= n or ny >= m: continue
        if visit[nx][ny] == 1: continue
        if a[nx][ny] == 0: continue
        dfs(nx,ny)

for _ in range(t):
    m, n, k = map(int, input().split()) # 가로, 세로
    visit = [[0]*m for _ in range(n)]
    a = [[0]*m for _ in range(n)] # 새로운 지도 맵
    # 양배추 위치 저장한 배열에 값 넣어주기
    for _ in range(k):
        y, x = map(int, input().split())
        a[x][y] = 1
    
    cnt  = 0
    for i in range(n):
        for j in range(m):
            if visit[i][j] == 1 or a[i][j] == 0: continue
            cnt +=1
            dfs(i,j)
    ans.append(cnt)

for res in ans:
    print(res)
            




"""
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
"""