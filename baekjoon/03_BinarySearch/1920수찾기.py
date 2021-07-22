
import sys
input = sys.stdin.readline

def lower_bound(lst, l, r, x):
    while l <=r :
        mid = (l+r)//2
        if lst[mid] == x:
            return True
        if lst[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return False


if __name__ == "__main__":
    n = int(input())
    nLst = sorted(list(map(int, input().split())))
    m = int(input())
    mLst = list(map(int, input().split()))
    # mLst값들이 aLst에 존재하면 1, 안하면 0 출력

    for candi in mLst:
        if lower_bound(nLst, 0, n-1, candi) :
            print(1)
        else:
            print(0)

