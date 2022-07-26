import sys
si = sys.stdin.readline

n = int(si())
lst = list(map(int, si().split()))
lst.sort()

v1, v2, v3 = 0, 0, 0
bestSum = 1<<31
for i in range(n-2):
    val = lst[i]
    l, r = i+1, n-1
    while l < r:
        nowSum = val + lst[l] + lst[r]
        if abs(bestSum) > abs(nowSum):
            bestSum = nowSum
            v1 = val
            v2 = lst[l]
            v3 = lst[r]
        if nowSum > 0: r-=1
        elif nowSum < 0 : l+=1
        else: break

print(v1, v2, v3) 


# 시간초과남