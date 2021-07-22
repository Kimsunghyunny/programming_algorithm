import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
visit = [0] * (n+1)

#인접행렬 만들기
a = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

def bfs(x):
    q = deque()
    q.append(x)
    visit[x] = 1

    while q:
        tmp = q.popleft()
        for y in a[tmp]:
            if visit[y]: continue
            q.append(y)
            visit[y] = 1

cnt = 0
for i in range(1, n+1):
    if visit[i]: continue
    bfs(i)
    cnt +=1
print(cnt)