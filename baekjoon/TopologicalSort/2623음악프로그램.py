import sys
from collections import deque
si = sys.stdin.readline

n, m = map(int, si().split())
adj = [[] for _ in range(n+1)]
indeg = [0] * (n+1)

# 그래프로 만들어 주기
for _ in range(m):
    a = list(map(int, si().split()))
    for i in range(1,a[0]):
        adj[a[i]].append(a[i+1])
        indeg[a[i+1]] += 1

# 싸이클을 돌 수 있는 그래프가 된다면 출연 순서를 정할 수 없어진다.
# 위상정렬을 이용하기 때문에 시간복잡도는 o(v+e)이다.
ans = []
def solve():
    q = deque()

    for i in range(1,n+1):
        if indeg[i] == 0 :
            q.append(i)

    while q:
        x = q.popleft()
        ans.append(x)
        for y in adj[x]:
            indeg[y] -= 1
            if indeg[y] == 0 :
                q.append(y)


solve()
if len(ans) == n:
    for result in ans:
        print(result)
else:
    print(0)
