import sys
import heapq
si = sys.stdin.readline


# 최단거리 dijkstra 사용하기
n, m = map(int, si().split())
adj = [[] for _ in range(n+1)]
dist = [1<<31] * (n+1)

for _ in range(m):
    a, b, c = map(int, si().split())
    adj[a].append([c,b]) #b까지의 소의 마리수 c
    adj[b].append([c,a])

def dijkstra():
    q = [[0,1]]
    dist[1] = 0

    while q:
        x = heapq.heappop(q)
        if dist[x[1]] < x[0]:continue
        for y in adj[x[1]]:
            if dist[x[1]] + y[0] >= dist[y[1]]:continue
            dist[y[1]] = dist[x[1]] + y[0]
            heapq.heappush(q,[dist[y[1]],y[1]])

dijkstra()
print(dist[n])

