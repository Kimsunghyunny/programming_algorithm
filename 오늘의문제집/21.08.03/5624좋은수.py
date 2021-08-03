import sys 
si = sys.stdin.readline

n = int(si())
a = list(map(int, si().split()))
visit = [0] * 400002
ans = 0

# a+b+c = d 일때, a+b = d-c라는 성질을 이용하자.
for i in range(n):
    for j in range(i):
        if visit[a[i]-a[j]+200000]:
            ans += 1
            break

    for j in range(i+1):
        visit[a[i]+a[j] + 200000] = 1

print(ans)