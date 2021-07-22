
import sys
si = sys.stdin.readline

n, q = map(int, si().split())
visited = [0] * (n+1)
ans = []
visit = set()
for i in range(q):
    x = int(si())
    isOwned, num, node = False, 0, x
    while node > 0:
        if node in visit:
            isOwned = True
            num = node
        node //= 2
    ans.append(num)
    if not isOwned:
        visit.add(x)

for i in ans:
    print(i)



## set을 쓰는게 시간복잡도는 더 좋지만, 공간복잡도는 성능이 떨어진다.
