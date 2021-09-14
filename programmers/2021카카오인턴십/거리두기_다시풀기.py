from collections import deque

def bfs(p, idx):
    visit = [[0]*5 for _ in range(5)]
    q = deque()
    q.append(idx)
    dirs = [[1,0],[-1,0],[0,1],[0,-1]]
    visit[idx[0]][idx[1]] = 1
    
    while q:
        curs = q.popleft()
        for dx, dy in dirs:
            nx, ny, nd = curs[0]+dx, curs[1]+dy, curs[2]+1
            if nx <0 or ny <0 or nx >= 5 or ny >= 5:continue
            if visit[nx][ny]:continue
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