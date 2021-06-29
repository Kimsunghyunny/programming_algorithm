
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    # 이분탐색 이용
    size = len(a)
    l, r = 0, a[size-1]

    while l <= r:
        mid = (l + r) // 2
        sum = 0
        for i in a:
            if i > mid:
                sum += i - mid
        if sum < m:
            r = mid - 1
        else:
            l = mid + 1
    print(r)