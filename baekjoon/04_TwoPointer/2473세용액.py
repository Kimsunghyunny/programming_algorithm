import sys
si = sys.stdin.readline

n = int(si())
lst = list(map(int, si().split()))
lst.sort()

v1, v2, v3 = 0, 0, 0
bestSum = 3*(10**9)  # long으로 선언 x시 틀림
flag = 0
for i in range(n-2):
    l, r = i+1, n-1
    while l < r:
        nowSum = lst[i] + lst[l] + lst[r]
        if bestSum > abs(nowSum):
            bestSum = abs(nowSum)
            v1 = lst[i]
            v2 = lst[l]
            v3 = lst[r]
        if nowSum > 0: r-=1
        elif nowSum < 0 : l+=1
        else: 
            flag = 1
            break

    if flag : break

print(v1, v2, v3) 