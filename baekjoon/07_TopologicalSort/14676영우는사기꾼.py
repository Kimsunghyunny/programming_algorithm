import sys
from collections import deque
si = sys.stdin.readline

n, m, k = map(int, si().split())
adj = [[] for _ in range(n+1)]
indeg = [0] * (n+1)
build = [0] * (n+1)
check = False

for _ in range(m):
    a, b = map(int, si().split())
    adj[a].append(b)
    indeg[b] += 1


for _ in range(k):
    c, d = map(int, si().split())

    if c == 1:
        if indeg[d] != 0:# 건물을 이전에 세워야 하는 건물을 다 짓고 세우는 경우가 아닌 케이스
            check = True
            break
        
        build[d] += 1

        if build[d] == 1:# 처음 건물을 세웠을 때
            for i in adj[d]:
                indeg[i] -= 1
    else:
        if build[d] <= 0:
            check = True
            break

        build[d] -= 1

        if build[d] == 0:
            for i in adj[d]:
                indeg[i] += 1

if check:
    print("Lier!")
else:
    print("King-God-Emperor")