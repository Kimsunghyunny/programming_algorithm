import sys
from collections import deque
si = sys.stdin.readline

n = int(si())
m = int(si())
adj = [[] for _ in range(n+1)]
result = [[0] * (n+1) for _ in range(n+1)]
indeg = [0] * (n+1)

for _ in range(m):
    x, y, k = map(int, si().split())
    # 중간부품이나 완제품 x를 만드는데 중간 부품 혹은 기본부품 y가 k개 필요하다.
    adj[y].append([x,k]) # adj에 [x,k]를 저장하여, x를 만들기위해 y가 k개 필요하다는 것을 저장
    indeg[x] += 1

def topologicalSort():
    q = deque()

    # 아무것도 필요하지 않은 기본부품
    for i in range(1,n+1):
        if indeg[i] == 0:
            q.append(i)

    while q:
        x = q.popleft()
        for y,w in adj[x]:
            # 만일 현 제품이 기본 부품인 경우에
            if result[x].count(0) == n+1:
                result[y][x] += w
            # 만일 현 제품이 중간 부품인 경우에
            else:
                for i in range(1,n+1):
                    result[y][i] += result[x][i] * w

            indeg[y] -= 1
            if indeg[y] == 0:
                q.append(y)

    for i in enumerate(result[n]):
        if i[1] > 0:
            print(i[0],i[1],sep=' ')
            #print(*i)도 가능

topologicalSort()

