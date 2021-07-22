import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
map = [input().strip() for _ in range(n)]
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
visit = [[0]*n for _ in range(n)]


def dfs(x, y):
    global group_cnt

    visit[x][y] = 1
    group_cnt += 1

    for dx, dy in dir:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if visit[nx][ny]:
            continue
        if map[nx][ny] == '0':
            continue
        dfs(nx, ny)


group_cnt = 0
group = []
for x in range(n):
    for y in range(n):
        if map[x][y] == '0' or visit[x][y] == 1:
            continue
        group_cnt = 0
        dfs(x, y)
        group.append(group_cnt)

group.sort()
print(len(group))
for g in group:
    print(g)