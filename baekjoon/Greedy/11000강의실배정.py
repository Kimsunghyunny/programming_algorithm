
import sys
import heapq

input = sys.stdin.readline

n = int(input())
time_table, heap = [], []

for _ in range(n):
    start, end = map(int, input().split())
    time_table.append([start, end])

time_table = sorted(time_table, key = lambda x : x[0])
heapq.heappush(heap, time_table[0][1])

for i in time_table[1:]:
    if heap[0] <= i[0]:
        heapq.heappushpop(heap, i[1])
    else:
        heapq.heappush(heap, i[1])
    
print(len(heap))