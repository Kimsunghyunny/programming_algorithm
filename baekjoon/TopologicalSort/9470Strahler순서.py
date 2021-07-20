import sys
from collections import deque
si = sys.stdin.readline


T = int(si())

def solve():
    q = deque()

    for i in range(1,m+1):
        if indeg[i] == 0:
            q.append(i)
            cnt[i] = [1,1]

    while q:
        x = q.popleft()
        if cnt[x][1] >= 2: # 들어오는 강의 개수가 2개 이상일때
            lv[x] = cnt[x][0] + 1
        else: # 들어오는 강의 개수가 1개이하 일때
            lv[x] = cnt[x][0]

        for y in adj[x]:
            indeg[y] -= 1
            if cnt[y][0] == lv[x]: # 만약 y로 들어오는 강의 개수가 lv[x]값과 같을때
                cnt[y][1] += 1
            elif cnt[y][0] < lv[x]: # 만약 y로 들어오는 강의 개수가 lv[x]값보다 작을때
                cnt[y] = [lv[x], 1]
            if indeg[y] == 0: # 들어오는 강의 수가 아무것도 없는 정점을 추가
                q.append(y)
    
    print(k,lv[m],sep=' ')


for _ in range(T):
    k, m, p = map(int, si().split())
    adj = [[] for _ in range(m+1)]
    indeg = [0] * (m+1)
    cnt = [[0,0] for _ in range(m+1)]
    lv = [0] * (m+1)

    # 인접리스트
    for _ in range(p):
        a, b = map(int, si().split())
        adj[a].append(b)
        indeg[b] += 1
    solve()