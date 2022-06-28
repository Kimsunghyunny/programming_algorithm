# 프로그래머스
# https://programmers.co.kr/learn/courses/30/lessons/67259
from collections import deque

def solution(board):
    
    n = len(board)
    ans = 1<<31
    dirs = [[1,0,0],[0,1,1],[-1,0,2],[0,-1,3]]
    dist = [[[1<<31 for _ in range(len(board[0]))] for _ in range(n)] for _ in range(4)]
    
    print(dist)
    
    q = deque()
    q.append([0,0,0,0])
    q.append([0,0,0,1])
    
    while q:
        cur = q.popleft()
        x, y, w, d = cur[0], cur[1], cur[2], cur[3]
        
        for dx, dy, dd in dirs:
            nx, ny = x + dx, y + dy
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n or board[ny][nx] != 0:
                continue
                
            nw = w + 1
            if d != dd:
                nw += 5
            if dist[dd][nx][ny] > nw:
                dist[dd][nx][ny] = nw
                if ny == n-1 and nx == n-1:
                    continue
                q.append([nx, ny, nw, dd])
    
    for i in range(4):
        ans = min(ans, dist[i][n-1][n-1])
    ans *= 100
    return ans





# 백준
# https://www.acmicpc.net/problem/4179
# 틀렸다는데 왜 틀린지 모르겟음
import sys
from collections import deque
si = sys.stdin.readline

r, c = map(int, si().split())
# python list만이 아래 코드처럼 값을 변경해줄 수 있다.
board = []

dirs = [[0,1],[0,-1],[1,0],[-1,0]]
ans = 'IMPOSSIBLE'
q = deque()

# 처음 시작되는 상황
for i in range(r):
    board.append(list(si().strip()))
    for j in range(c):
        if board[i][j] == 'J':
            q.append([0,i,j])
        elif board[i][j] == 'F':
            q.append([-1,i,j])

while q:
    cur = q.popleft()
    
    # 탈출성공
    if cur[0] > -1 and board[cur[1]][cur[2]] != 'F' and (cur[1] ==0 or cur[2] ==0 or cur[1] == r-1 or cur[2] == c-1):
        ans = cur[0] + 1
        break

    for dx, dy in dirs:
        nx, ny = cur[1] + dx, cur[2] + dy
        if nx < 0 or ny < 0 or nx >= r or ny >= c or board[nx][ny] == '#' or board[nx][ny] == '_':
            continue
        
        # 지훈 이동
        if cur[0] > -1 and board[nx][ny] == '.':
            board[nx][ny] = '_'
            q.append([cur[0]+1, nx, ny])
            
        # 불 이동
        elif cur[0] == -1 and board[nx][ny] == 'F':
            board[nx][ny] = 'F'
            q.append([-1, nx, ny])


print(ans)






# HackerRank
#https://joosjuliet.github.io/count_luck/