# 프로그래머스
# 스코빌 지수
# https://school.programmers.co.kr/learn/courses/30/lessons/42626?language=java

import heapq

def solution(scoville, K):
    res = 0
    q = []
    
    for i in scoville:
        heapq.heappush(q, i)
        
    while q[0] < K and len(q) >= 2:
        first = heapq.heappop(q)
        second = heapq.heappop(q)
        heapq.heappush(q, first+second*2)         
        res += 1
    return res if q[0] >= K else -1



# 프로그래머스
# 디스크
# https://school.programmers.co.kr/learn/courses/30/lessons/42627

import heapq

def solution(jobs):
    res, now, i = 0, 0, 0
    start = -1 
    heap = []
    
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        
        if len(heap) > 0:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            res += now - cur[1]
            i +=1
        else: 
            now += 1
                
    return res // len(jobs)