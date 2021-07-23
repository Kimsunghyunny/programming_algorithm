import sys
import heapq # 최소힙
si = sys.stdin.readline

n = int(si()) # 도시의 개수
m = int(si()) # 버스의 개수
dist = [1<<31] * (n+1)
edges = [[] for _ in range(n+1)]

for _ in range(m):
    f, t, w = map(int, si().split()) # from, to, weight
    edges[f].append([w,t])
start, end = map(int, si().split())

def dijkstra(start):
    q = [[0,start]]
    dist[start] = 0

    while q:
        x = heapq.heappop(q)
        
        # 새로운 x에 대한 값이 기존의 x[0]의 최소거리보다 더 크다면 가치가 없다.
        if dist[x[1]] < x[0]: continue 

        # x에 연결된 정점들을 돌아가며 각 정점에 대한 최소거리에 대해 갱신한다.
        for y in edges[x[1]]:
            # x부터 y까지 정점의 값을 더한게 기존 y에 대한 최소거리보다 크거나 같으면 넘어간다.
            if dist[x[1]] + y[0] >= dist[y[1]]: continue 
            
            # y의 최소거리가 더 작은 값을 찾았으니 새로 갱신한다.
            dist[y[1]] = dist[x[1]] + y[0]
            heapq.heappush(q, [dist[y[1]],y[1]])
            
dijkstra(start)
print(dist[end])