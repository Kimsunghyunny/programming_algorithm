"""

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.

--> 중복없이 고르기 -> o(n! / m!(n-m)!)

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
        if k == 0: start = 1
        else: start = lst[k-1]+1 # 이와 같은 if문을 통해서, 중복과 순서없이 고르는 것에 대해서 처리할 수 있다.
        for i in range(start, n+1):
            lst[k] = i
            solution(k+1)
            lst[k] = 0

solution(0)

