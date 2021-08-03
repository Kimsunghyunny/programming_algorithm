import sys
si = sys.stdin.readline

n = int(si())
m = int(si())
adj = [[1<<31]*(n+1) for _ in range(n+1)]
prev = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, si().split())
    if adj[a][b] > c:
        adj[a][b] = c
        prev[a][b] = a

#플로이드 워셜 알고리즘 o(n**3)
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i != j and adj[i][j] > adj[i][k]+adj[k][j]:
                adj[i][j] = adj[i][k]+adj[k][j]
                prev[i][j] = prev[k][j]

for i in adj[1:]:
    tmp = []
    for j in i[1:]:
        if j == 1<<31:
            tmp.append(0)
        else:
            tmp.append(j)
    print(*tmp)

for i in range(1,n+1):
    for j in range(1,n+1):
        if adj[i][j] == 1<<31:
            print(0)
        else:
            route = [j]
            tmp = j
            while tmp != i:
                route.append(prev[i][tmp])
                tmp = prev[i][tmp]

            print(len(route),end=' ')
            print(*route[::-1])


"""
def dijkstra(start):
    q = [[0,start]]
    dist[start] = 0

    while q:
        x = heapq.heappop(q)
        
        if dist[x[1]] < x[0]: continue

        for y in adj[x[1]]:
            if dist[x[1]]+y[0] >= dist[y[1]]:continue
            dist[y[1]] = dist[x[1]] + y[0]
            heapq.heappush(q,[dist[y[1]],y[1]])

for i in range(1,n+1):
    dist = [1<<31] * (n+1)
    path = [[] for _ in range(n+1)]
    path[i].append()
    dijkstra(i)
    for j in range(1,n+1):
        print(dist[j],end=' ')
    print()
"""