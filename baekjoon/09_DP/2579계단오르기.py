import sys
si = sys.stdin.readline

n = int(si())
step = [0] + [int(si()) for _ in range(n)]

# dp
dp = [[-1] * (n+1) for _ in range(n+1)]

dp[1][0] = 0
dp[1][1] = step[1]
if 2 <= n:
    dp[2][0] = step[2]
    dp[2][1] = dp[1][1] + step[2]

for i in range(3,n+1):
    dp[i][0] = max(dp[i-2][0]+step[i],dp[i-2][1]+step[i])
    dp[i][1] = dp[i-1][0] + step[i]

print(dp)
print(max(dp[n][0],dp[n][1]))