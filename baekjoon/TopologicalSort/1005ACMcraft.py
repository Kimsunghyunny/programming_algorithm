import sys
from collections import deque
si = sys.stdin.readline

T = int(si())

def solve():
    q = deque()

    for i in range(1,n+1):
        if indeg[i] == 0:
            q.append(i)
            done[i] = d[i-1]

    while q:
        x = q.popleft()
        for y in adj[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                q.append(y)
            done[y] = max(done[y], done[x] + d[y-1])

    w = int(si())
    print(done[w])

for _ in range(T):
    n, k = map(int, si().split())
    d = list(map(int, si().split()))
    done = [0] * (n+1)
    adj = [[] for _ in range(n+1)]
    indeg = [0] * (n+1)

    for _ in range(k):
        a, b = map(int, si().split())
        adj[a].append(b)
        indeg[b] += 1

    solve()
