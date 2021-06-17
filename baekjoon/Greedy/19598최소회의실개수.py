"""

import sys

input = sys.stdin.readline

n = int(input())

time_table = []

for _ in range(n):
    start, end = map(int, input().split())
    time_table.append([start, 1])
    time_table.append([end, -1])

time_table.sort()

ans = 0
usingRoom_cnt = 0

for _,i in time_table:
    usingRoom_cnt += i
    ans = max(ans, usingRoom_cnt)

print(ans)

"""


from sys import stdin
import heapq


N = int(stdin.readline())
meetings, heap = [], []

for i in range(N):
    start, end = map(int, stdin.readline().split())
    meetings += [[start, end]]

meetings = sorted(meetings, key = lambda k: k[0])
heapq.heappush(heap, meetings[0][1]) # meetings의 0번째값의 1번 값을 heap에 push한다.

for meeting in meetings[1:]: # mettings의 값에서 1부터 마지막값까지 넣는것.
    print(meeting)
    if heap[0] <= meeting[0]: # 현재 들어가있는 회의가 다음 미팅 시작시간보다 빠르거나 같다면 힙에 넣어준다.
        heapq.heappushpop(heap, meeting[1])
    else: # 현재 들어가있는 회의가 다음 미팅 시간보다 늦다면 힙에는 새로운 값을 넣어준다.
        heapq.heappush(heap, meeting[1])

print(len(heap))

## 해당 코드는 힙을 이용해서 시간을 정렬후 겹치는 여부를 확인하고 겹치지 않으면 값을뺀뒤에 새로운 값을 넣어주고, 겹친다면 새로운 값을 넣어주는 방식으로 해서
## 힙의 길이를 구하는것으로 답을 구하는 방법이다.  

## 첫번째 방법보다 시간이 빠르고 저장공간 메모리가 적은 이유는 첫번째 방법은 시간과 끝나는 시간 2개에 대해서 따로 저장하였기 때문에 비교시간과 메모리가 2배로 늘어날 수 밖에 없기떄문이다.