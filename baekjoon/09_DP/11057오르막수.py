import sys
si = sys.stdin.readline

n = int(si())

dp = [[0]*(10) for _ in range(n+1)]

#초기화
for i in range(10):
    dp[1][i] = 1

for i in range(2,n+1):
    for num in range(10):
        for prev in range(num+1):
            dp[i][num] += dp[i-1][prev]
            dp[i][num] %= 10007

ans = 0
for i in range(10):
    ans += dp[n][i]
    ans %= 10007

print(ans)