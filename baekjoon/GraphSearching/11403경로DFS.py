import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
#인접리스트 만들고 값을 받아옴
a = [list(map(int,input().split())) for _ in range(n)]
visit = [0] * n

def dfs(x):
    for i in range(n):
        if visit[i]: continue
        if a[x][i] == 0: continue
        visit[i] = 1
        dfs(i)

for i in range(n):
    dfs(i)
    for j in range(n):
        if visit[j]:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()
    visit = [0] * n