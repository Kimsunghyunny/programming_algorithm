"""

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

--> 중복 있게 고르기

"""

import sys
input = sys.stdin.readline

n,m = map(int, input().split())

lst = [0] * m

def solution(k):
    if k == m:
        for i in lst:
            print(i,end=' ')
        print()
    else:
        if k == 0:
            start = 1
        else:
            start = lst[k-1]
        for i in range(start, n+1):
            lst[k] = i
            solution(k+1)
            lst[k] = 0

solution(0)