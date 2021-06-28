import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    
    bestSum = 1 << 31
    v1, v2 = 0, 0
    for l in range(n-1):
        result = higher_bound(lst, l+1, n-1, -lst[l])
        if result - 1 > l and abs(lst[result-1]+lst[l]) < bestSum: # result -1 자리
            # result에 대한 조건을 앞에 먼저 둬서 out of index 예외를 처리함.
            bestSum = abs(lst[result-1] + lst[l])
            v1, v2 = lst[l], lst[result-1]
        if result < n and abs(lst[result]+lst[l]) < bestSum: # result 자리
            bestSum = abs(lst[result] + lst[l])
            v1, v2 = lst[l], lst[result]

    print(v1, v2)


def higher_bound(lst, l, r, x):
    res = r + 1
    while l <= r:
        mid = (l+r)//2
        if lst[mid] >= x:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res

if __name__ == "__main__":
    solve()    
