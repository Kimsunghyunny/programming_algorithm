import sys
from collections import deque
si = sys.stdin.readline

def bfs(x):
    q = deque()
    q.append(x)
    visit[x] = 1
    dist[x] = 0
    
    while q:
        cur = q.popleft()
        y = cur - 1
        if 0 <= y and y <= 100000 and visit[y] == 0:
            q.append(y)
            visit[y] = 1
            dist[y] = dist[cur] + 1
        y = cur + 1
        if 0 <= y and y <= 100000 and visit[y] == 0:
            q.append(y)
            visit[y] = 1
            dist[y] = dist[cur] + 1
        y = cur * 2
        if 0 <= y and y <= 100000 and visit[y] == 0:
            q.append(y)
            visit[y] = 1
            dist[y] = dist[cur] + 1
        

if __name__ == "__main__":
    n, k = map(int, si().split())
    visit = [0] * (100001)
    dist = [-1] * (100001)
    bfs(n)
    print(dist[k])