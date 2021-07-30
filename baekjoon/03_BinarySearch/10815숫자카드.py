import sys
si = sys.stdin.readline

n = int(si())
a = sorted(list(map(int, si().split())))
m = int(si())
b = list(map(int, si().split()))

def bs(x):
    l = 0
    r = len(a)-1
    res = 0
    while l <= r:
        mid = (l + r) // 2
        if a[mid] >= x:
            r = mid - 1
            res = mid
        else:
            l = mid + 1
    return res
        
#이분탐색으로 시간을 줄여 탐색하자. -> a가 정렬되어 있어야한다.
for i in b:
    idx = bs(i)
    if a[idx] == i:
        print(1,end=' ')
    else:
        print(0,end=' ')
    