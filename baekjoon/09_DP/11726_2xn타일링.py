import sys
si = sys.stdin.readline


def preprocess():
    dp[1] = 1
    dp[2] = 2

    for i in range(3,1001):
        dp[i] = (dp[i-2] + dp[i-1]) % 10007

n = int(si())
dp = [0] * (1001)
preprocess()
print(dp[n])
