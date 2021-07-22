import sys
from collections import deque
si = sys.stdin.readline

n = int(si())
adj = [[] for _ in range(n+1)]
indeg = [0] * (n+1)
buildSecond = [0] * (n+1)
ans = [0] * (n+1)

for i in range(1,n+1):
    a = list(map(int, si().split()))
    buildSecond[i] = a[0]
    for val in a[1:len(a)-1]:
        adj[val].append(i)
        indeg[i] += 1

def topologicalSort():
    q = deque()

    for i in range(1,n+1):
        if indeg[i] == 0:
            q.append(i)
            ans[i] = buildSecond[i]

    while q:
        x = q.popleft()
        for y in adj[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                q.append(y)
            ans[y] = max(ans[y], ans[x] + buildSecond[y])

topologicalSort()
for i in range(1,n+1):
    print(ans[i])
