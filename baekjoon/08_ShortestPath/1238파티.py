import sys
import heapq
si = sys.stdin.readline

n, m, x = map(int, si().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, t = map(int, si().split())
    adj[end].append([t,start])

def dijkstra(end):
    q = [[0,end]]
    dist[end] = 0
    
    while q:
        x = heapq.heappop(q)
        if dist[x[1]] < x[0]: continue
        for y in adj[x[1]]:
            if dist[x[1]] + y[0] >= dist[y[1]]: continue
            dist[y[1]] = dist[x[1]] + y[0]
            heapq.heappush(q,[dist[y[1]],y[1]])

ans = []
for i in range(1,n+1):
    dist = [1<<31] * (n+1)
    dijkstra(i)
    ans.append(dist[x])
dist = [1<<31] * (n+1)
dijkstra(x)
for i in range(n):
    ans[i] += dist[i+1]
print(max(ans))