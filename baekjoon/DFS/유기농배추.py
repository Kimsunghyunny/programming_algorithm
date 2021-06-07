

"""
유기농 배추에 대해서 단지 번호 붙이기에서 몇개의 단지가 존재하는지에 대해서 조사하는 구현을 해야한다.
대신, 테스트 케이스 여러개를 둔다는 것을 알고 있어야한다.
"""

import sys
# sys를 쓰는 이유는 반복되는 입력을 받을때, 시간초과가 날 수 있는 input이 아니라
# sys.stdin.readline()을 쓰기 위해서이다. 또한, input과 다르게 한줄을 그대로 받아오기에 split을 적절하게 사용할줄 알아야함.

def dfs(x,y):
    global cnt
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0 or visited[nx][ny]:
            continue
        if field[nx][ny] != 0:
            visited[nx][ny] = 1
            dfs(nx, ny)

if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 5) # python은 재귀 깊이가 1000으로 굉장이 얕다. 그렇기에 다음과 같이 설정해줘야 오류를 막을 수 있다.
    input = sys.stdin.readline # input에 대한 정의를 sys.stdin.realine으로 바꿔줌
    T = int(input())
    for _ in range(T):
        M, N, K = map(int,input().split())
        field = [[0] * M for _ in range(N)] ## field와 visited 리스트 초기화
        visited = [[0] * M for _ in range(N)]
        cnt = 0
        for _ in range(K):
            a, b = map(int,input().split())
            field[b][a] = 1
        for i in range(N):
            for j in range(M):
                if field[i][j] and not visited[i][j]:
                    visited[i][j] = 1
                    cnt += 1
                    dfs(i,j)
        print(cnt)



"""
tNum = int(input())

stack = []
cnt = 0

def dfs(m,n):
    global cnt

    a, b = stack.pop()
    if a >=0 and b >= 0 and a < m and b < n and loca[b][a] == 1:
        stack.append((b+1,a))
        stack.append((b-1,a))
        stack.append((b,a+1))
        stack.append((b,a-1))
        loca[b][a] = 0
        cnt += 1

for i in range(tNum):
    m, n , k = map(int, input().split()) # 가로 m, 세로 n, 유기농배추 위치 좌표 개수 k
    loca = [[0]*m for _ in range(n)] # loca 초기화
    lst = []

    for j in range(k):
        x, y = map(int, input().split())
        loca[y][x] = 1

    for a in range(m):
        for b in range(n):
            if loca[b][a] == 1:
                stack.append((b,a))
                while len(stack)>0:
                    dfs(m,n)
                lst.append(cnt)
                cnt = 0
    print(len(lst), end='\n')
"""