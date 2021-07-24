import sys
import heapq
si = sys.stdin.readline

v, e = map(int, si().split())
adj = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, si().split())
    adj[a].append([c,b])
    adj[b].append([c,a])

def dijkstra(start, end):
    dist = [1<<31] * (v+1)
    q = [[0,start]]
    dist[start] = 0

    while q:
        x = heapq.heappop(q)
        if dist[x[1]] < x[0]:continue
        for y in adj[x[1]]:
            if dist[x[1]] + y[0] >= dist[y[1]]:continue
            dist[y[1]] = dist[x[1]] + y[0]
            heapq.heappush(q,[dist[y[1]],y[1]])

    return dist[end]


stop1, stop2 = map(int, si().split())

path1 = dijkstra(1,stop1) + dijkstra(stop1, stop2) + dijkstra(stop2,v)
path2 = dijkstra(1,stop2) + dijkstra(stop2, stop1) + dijkstra(stop1, v)

if path1 >= 1<<31 and path2 >= 1<<31:
    print(-1)
else:
    print(min(path1,path2))



