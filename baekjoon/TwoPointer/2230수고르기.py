import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = sorted([int(input()) for _ in range(n)])

r, ans = 0, 1<<31

for l in range(n):
    while r + 1<n and lst[r]-lst[l] < m:
        r +=1

    if lst[r]-lst[l] >= m:
        ans = min(ans, lst[r]-lst[l])

print(ans)

# r을 0으로 할때와 -1로 할때의 차이점은 뭘까?