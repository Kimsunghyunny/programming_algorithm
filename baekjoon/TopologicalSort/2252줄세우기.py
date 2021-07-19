import sys
from collections import deque
si = sys.stdin.readline

n, m = map(int, si().split())
adj = [[] for _ in range(n+1)]
indeg = [0] * (n+1)
for _ in range(m):
    a, b = map(int, si().split())
    adj[a].append(b)
    indeg[b] += 1

# 위상정렬
visit = [0] * (n+1)
def sort():
    q = deque()
    
    for i in range(1,n+1):
        if indeg[i] == 0 :
            q.append(i)
    
    while q:
        x = q.popleft()
        print(x, end=' ')
        for y in adj[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                q.append(y)


sort()

    