import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    nLst, mLst = [], []
    nLst = sorted([input() for _ in range(n)])
    mLst = sorted([input() for _ in range(m)])

    def binary_search(arr, l, r, x):
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == x:
                return True
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return False

    ans = [candi for candi in mLst if binary_search(nLst, 0, n-1, candi)]
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i],end="")
