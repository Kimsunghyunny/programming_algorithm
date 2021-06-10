

"""

최대힙은 최소힙과 다르게 가장 첫번째 노드의 값이 가장 큰 값이 되어야한다는 것이다.

"""

import sys
import heapq as hq

input = sys.stdin.readline
n = int(input())
heap = []
ans = []

for i in range(n):
    val = int(input())
    if val:
        hq.heappush(heap, (-val, val))
        # 핵심 코드 부분. heap에 그냥 val을 넣을때는 최소힙을 만족하기 때문에 (-val, val)튜플로 힙 값을 넣어준다.
        # 즉, val값이 클수록 -val값은 작아지기 때문에 최소힙에 조건에서는 -val이 작을수록 가장 작은수로 인식되기 때문이다.
    else:
        ans.append(hq.heappop(heap)[1] if heap else 0)
    
sys.stdout.write('\n'.join(map(str, ans)))
