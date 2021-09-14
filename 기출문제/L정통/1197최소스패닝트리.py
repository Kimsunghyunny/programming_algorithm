import sys
import heapq
si = sys.stdin.readline

v, e = map(int, si().split())

adj = [[] for _ in range(v+1)]
heap = [[0,1]]
visit = [0] * (v+1)
for i in range(e):
    x, y, w = map(int, si().split())
    adj[x].append([w,y])
    adj[y].append([w,x])

ans = 0
cnt = 0
while heap:
    if cnt == v:
        break
    w ,y = heapq.heappop(heap)
    if visit[y]: continue
    visit[y] = 1
    ans += w
    cnt += 1
    for i in adj[y]:
        if visit[i[1]]:continue
        heapq.heappush(heap, i)
print(ans)
