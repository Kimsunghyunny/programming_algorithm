from functools import partial
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
adj = [[] for _ in range(n+1)]
parent = [0] * (n+1)

for _ in range(n-1):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

visit = [0] * (n+1)
def dfs(x):
    visit[x] = 1
    
    for y in adj[x]:
        if visit[y]: continue
        parent[y] = x
        dfs(y)


dfs(1)
for i in range(2, n+1):
    print(parent[i])

"""
7
1 6
6 3
3 5
4 1
2 4
4 7
    """