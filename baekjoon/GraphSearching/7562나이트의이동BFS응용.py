import sys
from collections import deque
si = sys.stdin.readline

T = int(si())

dirs = [[1,2],[2,1],[1,-2],[2,-1],[-1,2],[-2,1],[-1,-2],[-2,-1]]
ans = []

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visit[x][y] = 1
    dist[x][y] = 0

    while q:
        now = q.popleft()
        for dx, dy in dirs:
            nx, ny = now[0] + dx, now[1] + dy
            if nx < 0 or ny < 0 or nx >= l or ny >= l: continue
            if visit[nx][ny]: continue
            q.append([nx,ny])
            visit[nx][ny] = 1
            dist[nx][ny] = dist[now[0]][now[1]] + 1

for _ in range(T):
    l = int(si())
    cur = list(map(int, si().split()))
    goal = list(map(int, si().split()))
    visit = [[0]*l for _ in range(l)]
    dist = [[-1]*l for _ in range(l)]
    bfs(cur[0],cur[1])
    ans.append(dist[goal[0]][goal[1]])

for i in range(T):
    print(ans[i])

