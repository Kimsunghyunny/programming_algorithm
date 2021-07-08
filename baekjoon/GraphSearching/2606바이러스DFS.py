import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x):
    global cnt
    visit[x] = 1

    for y in a[x]:
        if visit[y]:continue
        dfs(y)
        cnt += 1
    

n = int(input())
m = int(input())
#인접행렬
a = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

visit = [0] * (n+1)
cnt = 0
dfs(1)
print(cnt)
