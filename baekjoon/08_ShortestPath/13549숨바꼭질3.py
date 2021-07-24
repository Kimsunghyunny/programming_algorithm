import sys
import heapq
si = sys.stdin.readline

n, k = map(int, si().split())
dist = [1<<31] * (100001)

def dijkstra(start,end):
    if end <= start:
        print(start-end)
        return

    q = [[0,start]]

    while q:
        x = heapq.heappop(q)
        for nx in [x[1]+1, x[1]-1, x[1]*2]:
            if 0 <= nx <= 100000:
                if nx == x[1]*2 and dist[nx] == 1<<31: # *2인경우에
                    dist[nx] = x[0]
                    heapq.heappush(q,[x[0],nx])
                elif dist[nx] == 1<<31: # +-1인 경우에
                    dist[nx] = x[0] + 1
                    heapq.heappush(q,[x[0]+1, nx])
    print(dist[k])

dijkstra(n,k)        