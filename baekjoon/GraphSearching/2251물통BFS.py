import sys
from collections import deque
si = sys.stdin.readline


limit = list(map(int, si().split()))

visit = [[[0]*205 for _ in range(205)] for _ in range(205)]
possible = [0] * 205

def bfs():
    def move(cur, f, t):
        res = [cur[0], cur[1], cur[2]]
        if cur[f] + cur[t] <= limit[t]:
            res[t] = res[t] + res[f]
            res[f] = 0
        else:
            res[f] -= limit[t]-res[t]
            res[t] = limit[t]
        return res

    q = deque()
    q.append([0,0,limit[2]])
    visit[0][0][limit[2]] = 1

    while q:
        now = q.popleft()
        if now[0] == 0: possible[now[2]] = 1
        for f in range(3):
            for t in range(3):
                if f == t: continue
                nxt = move(now,f,t)
                if visit[nxt[0]][nxt[1]][nxt[2]]: continue
                visit[nxt[0]][nxt[1]][nxt[2]] = 1
                q.append(nxt)

bfs()
for i in range(205):
    if possible[i]:
        print(i,end=' ')