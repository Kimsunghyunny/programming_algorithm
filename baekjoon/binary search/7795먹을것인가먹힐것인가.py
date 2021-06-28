

import sys
input = sys.stdin.readline

def solve():
    aSize, bSize = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    #이분탐색을 이용하자. 정렬된 배열이여야한다.
    b.sort() 

    ans = 0
    for aVal in a:
        ans += lower_bound(b, 0, bSize-1, aVal) + 1
        # +1을 해주는 이유는 lower_bound가 리턴하는 값은 aVal보다 작은 최대 원소의 배열번호이기 때문에, +1을 해줘야 갯수가 된다.
    print(ans)

def lower_bound(a, l, r, x):
    res = l -1 # 만일 l > r인 경우에는 -1을 return 하기 위해서 위와 같이.
    while l <= r:
        mid = (l+r) //2
        if a[mid] < x:
            res = mid
            l = mid + 1
        else:
            r = mid - 1    
    return res
    
if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        solve()
