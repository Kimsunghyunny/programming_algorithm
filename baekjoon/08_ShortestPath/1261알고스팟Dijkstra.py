import sys
import heapq
si = sys.stdin.readline

n, m = map(int, si().split())
a = [list(map(int,si().strip())) for _ in range(m)]
dirs = [[1,0],[-1,0],[0,1],[0,-1]]
visit = [[0] * n for _ in range(m)]
ans = 0
def dijkstra():
    global ans
    q = [[0,0,0]] # cnt, x, y
    visit[0][0] = 1
    
    while q:
        x = heapq.heappop(q)
        for dx, dy in dirs:
            nx, ny = x[1] + dx, x[2] + dy
            if x[1] == m-1 and x[2] == n-1:
                ans = x[0]
                break

            if nx < 0 or ny < 0 or nx >= m or ny >= n: continue
            if visit[nx][ny]: continue
            if a[nx][ny] == 1:
                heapq.heappush(q,[x[0] + 1, nx, ny])
            else:
                heapq.heappush(q,[x[0],nx,ny])
            visit[nx][ny] = 1

    print(ans)

dijkstra()
