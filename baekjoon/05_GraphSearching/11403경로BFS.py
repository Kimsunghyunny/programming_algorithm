import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    visit = [0] * n
    q = deque()
    q.append(x)
    #visit[x] = 1
    # 이 경우에는 위의 코드를 빼줘야한다. 위와같이 visit을 x에 체크해주면 자기자신에 대해서 당연히 방문할 수 있다는것으로 이해되기 때문에 삭제해줘야한다.

    while q:
        tmp = q.popleft()
        for i in range(n):
            if visit[i]: continue
            if a[tmp][i] == 0: continue
            q.append(i)
            visit[i] = 1
    for i in range(n):
        print(visit[i], end=' ')
    print() 

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    bfs(i)