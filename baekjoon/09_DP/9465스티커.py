import sys
si = sys.stdin.readline

T = int(si())

for _ in range(T):
    n = int(si())
    a = [list(map(int,si().split())) for _ in range(2)]
    a[0][1] += a[1][0]
    a[1][1] += a[0][0]
    for i in range(2,n):
        a[0][i] += max(a[1][i-1],a[1][i-2])
        a[1][i] += max(a[0][i-1],a[0][i-2])
    print(max(a[0][n-1],a[1][n-1]))