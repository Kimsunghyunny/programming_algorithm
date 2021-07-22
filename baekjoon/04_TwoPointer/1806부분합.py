import sys
si = sys.stdin.readline
n, S = list(map(int, si().split()))
a = list(map(int, si().split()))
R, sum, ans = -1, 0, n + 1
for L in range(n):
    print("l=",L,end=' ')
    while R + 1 < n and sum < S:
        R += 1
        print("r=",R,end=' ')
        sum += a[R]
    print("sum=",sum,end=' ')
    if sum >= S:
        print("ans=",ans)
        ans = min(ans, R - L + 1)

    sum -= a[L]

if ans == n + 1: ans = 0
print(ans)