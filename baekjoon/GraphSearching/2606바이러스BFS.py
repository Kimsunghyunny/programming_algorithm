import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    global cnt
    q = deque()
    q.append(x)
    visit[x] = 1

    while q:
        tmp = q.popleft()
        for y in a[tmp]:
            if visit[y]:continue
            q.append(y)
            visit[y] = 1
            cnt += 1


n = int(input())
m = int(input())
a = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

visit = [0] * (n+1)    
cnt = 0
bfs(1)
print(cnt)

