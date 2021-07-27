import sys
si = sys.stdin.readline

n = list(map(int, si().strip()))
l = len(n)
dp = [0] * (l+1)

# dp
if n[0] == 0: print(0)
else:
    n = [0] + n
    dp[0], dp[1] = 1, 1
    for i in range(2,l+1):
        if int(n[i]) > 0:
            dp[i] += dp[i-1]
            dp[i] %= 1000000
        tmp = int(n[i-1])*10 + int(n[i])
        if 10 <= tmp and tmp <= 26:
            dp[i] += dp[i-2]
            dp[i] %= 1000000
    print(dp[l])