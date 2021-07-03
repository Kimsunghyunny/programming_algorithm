import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
count = [0] * (100000 + 1)

ans = 0

r = -1

for l in range(n):
    while r + 1 < n and count[lst[r+1]] != 1:
        r += 1
        count[lst[r]] += 1


    ans += r - l + 1
    count[lst[l]] -= 1

print(ans)