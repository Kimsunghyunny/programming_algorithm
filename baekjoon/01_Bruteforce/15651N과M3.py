
"""

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.

--> 중복가능, 순서있게 나열  --> 시간복잡도 (o(N^M))

"""

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
lst = [0] * m

def solution(k):
    if k == m: #m개를 모두 선택했을 때
        for val in lst:
            print(val, end='')
        print()
    else: # m개를 아직 모두 선택하지 못했을 때
        for i in range(1,n+1): #n까지 반복문을 돌아가며 선택
            lst[k] = i
            solution(k+1)
            lst[k] = 0
        

if __name__ == "__main__":
    solution(0)
