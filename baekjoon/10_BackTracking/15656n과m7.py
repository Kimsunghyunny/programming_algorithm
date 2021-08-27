import sys
si = sys.stdin.readline

n, m = map(int, si().split())
arr = list(map(int, si().split()))
arr.sort()
visit = [0] * n
ans = []
anslst = []
    
def dfs(d):

    if d == m:
        tmp = ' '.join(map(str,ans))
        print(tmp)
        return
    check = 0
    for i in range(n):
        if visit[i]:continue
        if check == arr[i]:continue
        print(i, arr[i], check)
        visit[i] = 1
        ans.append(arr[i])
        check = arr[i]
        dfs(d+1)
        ans.pop()
        visit[i] = 0

dfs(0)