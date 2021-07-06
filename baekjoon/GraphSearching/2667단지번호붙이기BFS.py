import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = [input().strip() for _ in range(n)]
visit = [[0]*n for _ in range(n)]
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

group_cnt = 0


def bfs(x, y):
    global group_cnt

    q = deque()
    q.append((x, y))
    visit[x][y] = 1
    group_cnt += 1

    while q:
        now = q.popleft()
        for dx, dy in dir:
            nx, ny = now[0] + dx, now[1] + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visit[nx][ny] == 1:
                continue
            if a[nx][ny] == '0':
                continue
            q.append((nx, ny))
            visit[nx][ny] = 1
            group_cnt += 1


group = []
for x in range(n):
    for y in range(n):
        if visit[x][y] == 1 or a[x][y] == '0':
            continue
        group_cnt = 0
        bfs(x, y)
        group.append(group_cnt)

group.sort()
print(len(group))
for g in group:
    print(g)
