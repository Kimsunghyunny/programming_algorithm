import sys
from collections import deque
si = sys.stdin.readline

n = int(si())
adj = [[] for _ in range(n+1)]
indeg = [0] * (n+1)
time = [0] * (n+1)
ansTime = [0] * (n+1)

# adj, indeg 추가
for i in range(1,n+1):
    a = list(map(int, si().split()))
    time[i] = a[0]
    for j in a[2:]:
        adj[j].append(i)
        indeg[i] += 1

def topologicalSort():
    global ans
    q = deque()

    for i in range(1, n+1):
        if indeg[i] == 0:
            q.append(i)
            ansTime[i] = time[i]

    while q:
        x = q.popleft()
        for y in adj[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                q.append(y)
            ansTime[y] = max(ansTime[y], ansTime[x]+time[y])

topologicalSort()
print(max(ansTime))


