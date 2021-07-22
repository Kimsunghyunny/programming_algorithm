


## *주의 이 방법으로 하면 o(n**2)이기에 2초가 넘어 시간초과가 발생한다.

import sys
si = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(si())
adj = [[] for _ in range(n+1)]
visit = [0] * (n+1)
for _ in range(n-1):
    x, y = map(int, si().split())
    adj[x].append(y)
    adj[y].append(x)

# 단말노드의 개수를 찾아 홀수이면 성원이 승, 짝수이면 형석이 승
cnt = 0
def dfs(x, depth):
    global cnt
    visit[x] = 1
    if x != 1 and len(adj[x]) == 1: # 리프노드인 조건
        cnt += depth
    else:
        for y in adj[x]:
            if visit[y]: continue
            dfs(y, depth + 1)

dfs(1, 0)

if (cnt % 2) == 1:
    print("YES")
else:
    print("NO")