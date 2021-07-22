import sys
input = sys.stdin.readline

# i번재부터 j번째까지의 값이 m이 되는 경우의 수 구하기

n, m = map(int, input().split())
lst = list(map(int, input().split()))

r, sum, ans = -1, 0, 0

for l in range(n):
    while r + 1 < n and sum < m:
        r += 1
        sum += lst[r]

    if sum == m:
        ans += 1

    sum -= lst[l]

print(ans)

    