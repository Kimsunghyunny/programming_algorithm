import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

r, sum, ans = -1, 0, -1

for l in range(n-k+1):
    while r + 1 < n and sum < k:
        r += 1
        if lst[r] == 1:
            sum += 1

    if sum == k:
        if ans == -1:
            ans = r - l + 1
        else:
            ans = min(ans, r-l+1)

    if lst[l] == 1:
        sum -= 1

print(ans)
