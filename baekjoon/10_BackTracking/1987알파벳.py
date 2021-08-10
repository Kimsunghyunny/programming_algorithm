import sys
si = sys.stdin.readline

r, c = map(int, si().split())
arr = [si().strip() for _ in range(r)]
ch = [0] * 26
ans = 0
#백 트래킹
dirs = [[1,0],[-1,0],[0,1],[0,-1]]
def dfs(x,y,cnt):
    global ans
    ans = max(ans, cnt)

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= r or ny >= c: continue
        if ch[ord(arr[nx][ny])-65]: continue
        ch[ord(arr[nx][ny])-65] = 1
        dfs(nx,ny,cnt+1)
        ch[ord(arr[nx][ny])-65] = 0

ch[ord(arr[0][0])-65] = 1
dfs(0,0,1)
print(ans)
    