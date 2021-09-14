import sys
si = sys.stdin.readline
sys.setrecursionlimit(10**9)

t = int(si())

def pick(flag, i, j):
    if i > j : return 0
    if dp[i][j]: return dp[i][j]
    
    if flag:
        score = max(pick(0, i+1, j)+cardlst[i], pick(0, i, j-1)+cardlst[j])
        dp[i][j] = score
        return score
    else:
        score = min(pick(1,i+1,j),pick(1,i,j-1))
        dp[i][j] = score
        return score

for i in range(t):
    n = int(si())
    cardlst = list(map(int,si().split()))
    dp = [[0 for _ in range(n)] for _ in range(n)]
    pick(1, 0, n-1)
    print(dp[0][n-1])