"""

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

--> 중복없이, 순서있게 나열 --> 시간복잡도 O(n! / (n-m)!)

"""

import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().split())

    lst = [0] * m
    used = [0] * (n+1)

    def solution(k):
        if k == m:
            for i in lst:
                print(i, end='')
            print()
        else:
            for i in range(1,n+1):
                if used[i] == 1:
                    continue
                else:
                    lst[k] = i
                    used[i] = 1
                    solution(k+1)
                    lst[k] = 0
                    used[i] = 0
    
    solution(0)
                

if __name__ == "__main__":
    main()