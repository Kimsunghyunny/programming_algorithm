import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


r, c = map(int, input().split()) # r은 행 c는 열의 길이
a = [list(input().strip()) for _ in range(r)]

visit = [[0]*c for _ in range(r+1)]
dirs = [[1,0],[-1,0],[0,1],[0,-1]]

sheep = 0
wolf = 0

def dfs(x,y):
    global sheep, wolf
    if a[x][y] == 'o': sheep += 1
    elif a[x][y] == 'v': wolf += 1
    visit[x][y] = 1

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= r or ny >= c: continue
        if a[nx][ny] == '#': continue
        if visit[nx][ny]: continue
        dfs(nx,ny)

ansSheep = 0
ansWolf = 0
for i in range(r):
    for j in range(c):
        if a[i][j] == '#': continue
        if visit[i][j]: continue
        dfs(i,j)
        #print("i=",i,"j=",j,"sheep=",sheep,"wolf=",wolf)
        if sheep <= wolf:
            ansWolf += wolf
        else:
            ansSheep += sheep
        sheep, wolf = 0, 0

print(ansSheep, ansWolf, sep =' ')


