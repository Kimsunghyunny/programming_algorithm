import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

r, sum, ans = -1, 0, -(1<<31)

for l in range(n-k+1):
    print("l=",l,end=' ')
    while r + 1 < l + k and r + 1 < n:
        r += 1
        sum += lst[r]
        print("r=",r,end=' ')
        
    ans = max(ans, sum)
    print("sum=",sum)
    
    sum -= lst[l]

print(ans)