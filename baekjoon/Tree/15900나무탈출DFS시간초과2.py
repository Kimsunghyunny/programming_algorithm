


## *기존에 방식에 시간초과 나는 것에 대해서 isLeaf를 추가해 초과가 나지 않게한다.

import sys
si = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(si())
adj = [[] for _ in range(n+1)]
visit = [False] * (n+1)
for _ in range(n-1):
    x, y = map(int, si().split())
    adj[x].append(y)
    adj[y].append(x)

# 단말노드의 개수를 찾아 홀수이면 성원이 승, 짝수이면 형석이 승
cnt = 0
def dfs(x, depth):
    global cnt
    visit[x] = True
    isLeaf = True

    for y in adj[x]:
        if visit[y]: continue
        dfs(y, depth + 1)
        isLeaf = False
    
    if isLeaf:
        cnt += depth

dfs(1, 0)
print("Yes" if (cnt%2)==1 else "No")



#아래의 방식과 같은 방식이지만, 위의 부분에서는 왜인지 모르겠지만 시간초과가 난다. 아마 아래의 코드고 아슬아슬하게 2초이내로 실행이 되기 때문에 변수선언이나 이런데에 있어서 차별점이 있기 때문에 그런것같다.
"""
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(read())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, read().split())
    tree[a].append(b)
    tree[b].append(a)

total_cnt = 0
visited = [False] * (n+1)
def backtracking(node, cnt):
    global total_cnt
    visited[node] = True
    is_leaf = True
    for child in tree[node]:
        if not visited[child]:
            backtracking(child, cnt+1)
            is_leaf = False
    if is_leaf:
        total_cnt += cnt

backtracking(1, 0)
print('Yes' if total_cnt % 2 == 1 else 'No')



"""

