from collections import deque

def bfs(x,y,place):
    q = deque()
    q.append(x)
    q.append(y)
    
    dirs = [[1,0],[-1,0],[0,1],[0,-1]]
    
    visit = [[0] * 5 for _ in range(5)]
    visit[x][y] = 1
    
    dist = 2
    while q and dist > 0 :
        size = len(q)
        dist -= 1
        while size :
            tmpX = q.popleft()
            tmpY = q.popleft()
            size -= 2
            for dx, dy in dirs:
                nx, ny = tmpX + dx, tmpY + dy
                if nx < 0 or ny < 0 or nx >= 5 or ny >= 5: continue
                if visit[nx][ny]: continue
                if place[nx][ny] == 'P':
                    return False
                elif place[nx][ny] == 'O':
                    visit[nx][ny] = 1
                    q.append(nx)
                    q.append(ny)
                
    return True
    
    
def solution(places):
    
    # 거리두기 각 place 대기실당 거리두기가 지켜지고 있는지 확인
    # 맨해튼 거리는 |r1-r2|+|c1-c2|이며 이것이 3이상이여야 거리두기가 제대로 된것이다.
    
    ans = []
    
    for place in places:
        start = []
        check = True
        for x in range(5):
            for y in range(5):
                if place[x][y] == 'P':
                    start.append([x,y])
                    
        for cur in start:
            check = bfs(cur[0],cur[1],place)
            if not check:
                break
                
        if check:
            ans.append(1)
        else:
            ans.append(0)
    
    return ans



