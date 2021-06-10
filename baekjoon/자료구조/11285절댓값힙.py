

import sys
import heapq as hq


input = sys.stdin.readline

n = int(input())

heap = []
ans = []

for i in range(n):
    x = int(input())
    if x:
        if x > 0:
            hq.heappush(heap, (x, x))
        else:
            hq.heappush(heap, (-x, x))
    else:
        ans.append(hq.heappop(heap)[1] if heap else 0)

sys.stdout.write('\n'.join(map(str,ans)))

