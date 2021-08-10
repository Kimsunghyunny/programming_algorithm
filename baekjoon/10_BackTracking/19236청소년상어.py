import sys
import copy
si = sys.stdin.readline

tmp = [list(map(int, si().split())) for _ in range(4)]
arr = [[0] * 4 for _ in range(4)]
for i in range(4):
    for j in range(4):
        arr[i][j] = [tmp[i][j*2],tmp[i][j*2+1]-1]
dirs = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]

def sharkmove(a, x, y):
    posi = []
    sharkdir = a[x][y][1]
    for _ in range(3):
        nx, ny = x + dirs[sharkdir][0], y + dirs[sharkdir][1]
        if 0 <= nx < 4 and 0 <= ny < 4 and 1<= a[nx][ny][0] <= 16:
            # 이미 먹힌 물고기는 번호가 -1이므로 a[nx][ny][0] 값도 확인해줘야한다.
            posi.append([nx,ny])
        x, y = nx, ny
    return posi

def findFish(a, idx):
    for i in range(4):
        for j in range(4):
            if a[i][j][0] == idx:
                return (i,j)
    return None

def move(a, x, y):
    posi = []
    for i in range(1, 17):
        posi = findFish(a,i)
        if posi == None:
            continue
        fishX, fishY = posi[0], posi[1]
        fishDir = a[fishX][fishY][1]
        for _ in range(8):
            nx, ny = fishX + dirs[fishDir][0], fishY + dirs[fishDir][1]
            if 0 <= nx < 4 and 0<= ny < 4: 
                if not (nx == x and ny == y):# x, y 는 상어가 있는 위치
                    tmp = a[fishX][fishY][0]
                    a[fishX][fishY][0], a[nx][ny][0] = a[nx][ny][0], tmp
                    a[fishX][fishY][1], a[nx][ny][1] = a[nx][ny][1], fishDir
                    break
            fishDir = (fishDir+1) % 8 # 안된다면 45도 각도 움직여야한다      


def dfs(a, x, y, cnt):
    global ans
    a = copy.deepcopy(a)
    
    num = a[x][y][0]
    a[x][y][0] = -1
    
    # 물고기 이동
    move(a, x, y)

    # 상어가 이동할 수 있는 위치 후보들
    # 백트래킹을 하는 과정. 상어가 갈 수 있는 여러 위치에 대해서 각각 dfs를 실행해 가장 큰 값을 ans에 저장하도록 한다.
    res = sharkmove(a,x,y)
    ans = max(ans, cnt + num)
    for nx, ny in res:
        dfs(a, nx, ny, cnt + num)


ans = 0
dfs(arr, 0, 0, 0)
print(ans)