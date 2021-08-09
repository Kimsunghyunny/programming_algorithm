import sys
si = sys.stdin.readline

l, c = map(int ,si().split())
arr = sorted(list(map(str, si().split())))
visit = [0] * c
# a,e,i,o,u는 모음. 최소 모음 1개와 자음 2개
ans = []

def dfs(idx, length):
    if length == l:
        a = 0 # 모음
        b = 0 # 자음
        for i in range(l):
            if ans[i] in 'aeiou':
                a += 1
            else:
                b += 1
        if a >= 1 and b >= 2:
            print(''.join(ans))
        return
    for i in range(idx, c):
        if visit[i]:continue
        ans.append(arr[i])
        visit[i] = 1
        dfs(i+1, length+1)
        visit[i] = 0
        del ans[-1]
        
dfs(0,0)
