import sys
si = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, si().split())
a = list(map(int, si().split()))
adj = [[] for _ in range(n+1)] # adj는 해당 번호의 부하 번호를 저장
for i in range(1,n):
    adj[a[i]].append(i+1)
dist = [0] * (n+1)

def dfs(start):
    for y in adj[start]:
        dist[y] += dist[start]
        dfs(y)

for _ in range(m):
    a, b = map(int, si().split())
    dist[a] += b

dfs(1)
for i in range(1,n+1):
    print(dist[i],end=' ')
