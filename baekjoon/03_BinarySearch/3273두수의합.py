import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    lst = sorted(list(map(int, input().split())))
    x = int(input())

    # 이분탐색할대, x-a(i) 값을 탐색하는 것으로 한다.
    def binary_search(arr, l , r, x):
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == x:
                return True
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return False

    ans = 0

    for i in range(n):
        result = binary_search(lst, i + 1, n - 1, x - lst[i])
        if result: ans += 1
    

    print(ans)
