import sys
si = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, r, q = map(int, si().split())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, si().split())
    adj[a].append(b)
    adj[b].append(a)
qLst = [int(si()) for _ in range(q)]
visit = [False] * (n+1)
subtree = [0] * (n+1)

def dfs(root):
    visit[root] = True
    subtree[root] = 1

    for y in adj[root]:
        if visit[y]:continue
        dfs(y)
        subtree[root] += subtree[y]

dfs(r)

for i in qLst:
    print(subtree[i])
