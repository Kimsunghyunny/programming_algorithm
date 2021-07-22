from functools import update_wrapper
import sys
input = sys.stdin.readline

def lower_bound(arr, l, r, x): # x이상인 것들 중에서 가장 작은 값의 위치 찾기
    res = r + 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] >= x:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res

def upper_bound(arr, l, r, x): # x이하인 것들 중에서 가장 큰 값의 위치값 찾기
    res = r + 1 # 아무것도 갱신되지 않는다면 r+1값을 return 하고싶기 때문에 r+1을 초기값으로 두게된다.
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] > x:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res

n = int(input())
nLst = sorted(list(map(int,input().split())))
m = int(input())
mLst = list(map(int,input().split()))

for x in mLst:
    print(upper_bound(nLst, 0, n-1, x) - lower_bound(nLst, 0, n-1, x), end=' ')
