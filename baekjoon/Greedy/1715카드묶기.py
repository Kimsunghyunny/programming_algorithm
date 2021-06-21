

import sys, heapq
input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    heapq.heappush(heap, int(input()))

ans = 0

if N != 1:
    while len(heap) > 1 :
        fst = heapq.heappop(heap)
        snd = heapq.heappop(heap)
        sumVal = fst + snd
        ans += sumVal
        heapq.heappush(heap, sumVal)

print(ans)