# 프로그래머스
# 거리두기
# https://school.programmers.co.kr/learn/courses/30/lessons/81302

from collections import deque

def bfs(p, idx):
    
    visit = [[0]*5 for _ in range(5)]
    dirs = [[1,0],[-1,0],[0,1],[0,-1]]
    q = deque()
    q.append([idx[0],idx[1],idx[2]])
    visit[idx[0]][idx[1]] = 1
    
    while q:
        cur = q.popleft()
        for dx, dy in dirs:
            nx, ny, nd = cur[0] + dx, cur[1] + dy, cur[2] + 1
            if nx < 0 or ny < 0 or nx >= 5 or ny >=5 : continue
            if visit[nx][ny]: continue
            visit[nx][ny] = 1
            if p[nx][ny] == 'P':
                if nd <= 2:
                    return 0
            elif p[nx][ny] == 'O':
                if nd == 1:
                    q.append([nx,ny,nd])
    
    return 1

def solution(places):
    
    ans = []
    for p in places:
        flag = 1
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    res = bfs(p, [i,j,0])
                    if not res:
                        flag = 0
        ans.append(flag)

    
    return ans





# 프로그래머스
# 삼각달팽이
# https://school.programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    
    res = [[0 for j in range(1, i+1)] for i in range(1,n+1)]
    x = -1
    y = 0
    num = 1
    
    for i in range(n): # 방향 n번 회전
        for j in range(i, n) :
            if i % 3 == 0 :
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            res[x][y] = num
            num += 1
    
    return sum(res, [])
