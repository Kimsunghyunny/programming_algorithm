import sys
si = sys.stdin.readline

ans = []
while True:
    n, k = map(int, si().split())
    if n == 0 and k == 0:
        break
    a = list(map(int, si().split()))
    cnt, idx = -1, 0
    p = [-1] * 20

    for i in range(n):
        if a[i] == k:
            idx = i
        if a[i] != a[i-1] + 1:
            cnt += 1
        p[i] = cnt

    print(idx)
    print(p)
    ans = 0
    for i in range(1,n):
        if p[i] != p[idx] and p[p[i]] == p[p[idx]]: # par은 다르지만 par끼리는 형제인경우
            ans += 1

    print(ans)
    
        
"""
10 15
1 3 4 5 8 9 15 30 31 32
12 9
3 5 6 8 9 10 13 15 16 22 23 25
10 4
1 3 4 5 8 9 15 30 31 32

"""