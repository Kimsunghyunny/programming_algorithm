import sys
si = sys.stdin.readline

n, m = map(int, si().split())
arr = list(map(int, si().split()))
arr.sort()
ans = []

def dfs(d, idx):

    if d == m:
        print(*ans)
        return
    for i in range(idx,n):
        ans.append(arr[i])
        dfs(d+1, i+1)
        ans.pop()

dfs(0,0)