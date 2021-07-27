import sys
si = sys.stdin.readline

n = int(si())
a = [int(si()) for _ in range(n)] +[0,0]

dp = [0] * (n+2)
# a와 dp에 +2를 해주는 이유는 dp를 0~2까지 초기화 해주었기 때문이다.

dp[0] = a[0]
dp[1] = a[0]+a[1]
dp[2] = max(a[2]+a[0], a[2]+a[1], dp[1])
for i in range(3,n):
    dp[i] = max(dp[i-2]+a[i], a[i]+a[i-1]+dp[i-3],dp[i-1])

print(max(dp))