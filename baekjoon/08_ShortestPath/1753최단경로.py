import sys
import heapq
si = sys.stdin.readline


def dijkstra(start):
    q = [[0, start]] # 최소힙을 사용할때, 우선순위 기준이 되는 값을 첫번째 인자 값으로 두게해야한다.
    dist[start] = 0

    while q:
        x = heapq.heappop(q)
            #아래의 if문에 대해서는 예를들어서 이미 3정점에 대한 최단거리가 17인데 q에 (3,22)가 있어서 x[1]가 22일때는
            #최단거리보다 이미 값이 크기때문에 더이상 실행시키지 않아도 되는 것이다.
        if dist[x[1]] < x[0]:
                continue

            # 연결된 정점들에 대해서 최단거리인지를 판별하고 갱신해준다.
        for y in adj[x[1]]:
            if dist[x[1]] + y[0] >= dist[y[1]]:
                    continue
            dist[y[1]] = dist[x[1]] + y[0]
            heapq.heappush(q, [dist[y[1]],y[1]])

v, e = map(int, si().split())
k = int(si())  # 시작점
adj = [[] for _ in range(v+1)]
INF = sys.maxsize
dist = [INF]*(v+1)
for _ in range(e):
    u, m, w = map(int, si().split())
    adj[u].append([w, m])

dijkstra(k)
for i in range(1,v+1): print("INF" if dist[i] == INF else dist[i])