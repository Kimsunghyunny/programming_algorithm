import sys
si = sys.stdin.readline

T = int(si())
dp = [0] * (1000001)

def preprocess():
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4,1000001):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

preprocess()
for _ in range(T):
    n = int(si())
    print(dp[n])

