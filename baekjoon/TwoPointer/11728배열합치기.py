import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

l, r, ans = 0, 0, []

while l < n and r < m:
    if a[l] > b[r]:
        ans.append(b[r])
        r += 1
    else:
        ans.append(a[l])
        l += 1

while l < n:
    ans.append(a[l])
    l += 1
while r < m:
    ans.append(b[r])
    r += 1

print(" ".join(map(str, ans)))
