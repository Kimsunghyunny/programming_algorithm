# 프로그래머스
# https://programmers.co.kr/learn/courses/30/lessons/12978


# 양방향
# k시간 이하로 배달시간이 있는곳만 배달 주문을 받는다.
# res = 1번마을에서 k이하 시간에 배달이 가능한 마을의 개수

import heapq
from tkinter import dialog

def solution(N, road, K):
    # 마을의 번호는 1번부터이니, n+1개로 만들어주자
    adj = [[] for _ in range(N+1)]
    dist = [1<<31] * (N+1)
    
    for i in road:
        adj[i[0]].append([i[2], i[1]])
        adj[i[1]].append([i[2], i[0]])
        
    q = [[0,1]]
    dist[1] = 0
    
    while q:
        x = heapq.heappop(q)
        if dist[x[1]] < x[0]:continue
        for y in adj[x[1]]:
            if dist[x[1]] + y[0] >= dist[y[1]]:continue    
            dist[y[1]] = dist[x[1]] + y[0]
            heapq.heappush(q, [dist[y[1]], y[1]])
                    
    res = 0
    for i in range(1,N+1):
        if dist[i] <= K:
            res += 1
            
    return res






# 백준
# https://www.acmicpc.net/problem/1238

# 단방향 도로

import sys
import heapq
si = sys.stdin.readline

n, m, x = map(int, si().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, t = map(int, si().split())
    adj[end].append([t,start])

def dikstra(start):
    q = [[0,start]]
    dist = [1<<31] * (n+1)
    dist[end] = 0

    while q:
        x = heapq.heappop(q)
        if dist[x[1]] < x[0] : continue
        for y in adj[x[1]]:
            if dist[y[1]] + x[0] >= y[0]:continue
            dist[y[1]] = dist[y[1]] + x[0]
            heapq.heappush(q, [dist[y[1]], y[1]])

res = 0
for i in range(1, n+1):
    go = dikstra(i)
    back = dikstra(x)
    res = max(res, go[x]+back[i])

print(res)






# 해커랭크
# https://www.hackerrank.com/challenges/find-the-nearest-clone/problem

# 최단거리로 되어있지만, 가중치나 거리가 다른경우가 아니기 때문에 그래프 탐색으로 해결

import sys
from collections import deque
si = sys.stdin.readline

n, m = map(int, si().split())
adj = [[]for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, si().split())
    adj[s].append(e)
    adj[e].append(s)
color = si().split()
findVal = int(si())

q = deque()
q.append([findVal, 0])
stColor = color[findVal-1]

visited = [0] * (n+1)
flag = 0
while q:
    cur = q.popleft()
    visited[cur[0]] = 1

    if color[cur[0]-1] == stColor and cur[0] != findVal:
        flag = 1
        print(cur[1])
        break
    for x in adj[cur[0]]:
        if visited[x] == 1: continue
        # 아래의 조건문은 할필요가 없었음
        # if color[x-1] != stColor: continue
        visited[x] = 1
        q.append([x,cur[1]+1])

if flag == 0:
    print(-1)