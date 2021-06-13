

import sys

input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(21)]

dp[0] = 1
dp[1] = 1

for i in range(2, 21):
    if i % 2 == 0: # 짝수일때
        dp[i] = dp[i-1] * 2 - dp[i-5] - dp[i-4]
    else: # 홀수일때
        dp[i] = dp[i-1] * 2

print(dp[n])