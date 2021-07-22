"""

N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

--> 중복 없이 순서 있게 고르기

그러나 이와 같은 방법으로 하면 n이 12,13일때부터 시간초과가 나게 된다.
왜냐하면 재귀함수를 사용하기 때문에 (1*1)*(2*2)*....(12*12)*(13*13)..와 같은 식으로 늘어나기 때문이다.

"""

import sys
input = sys.stdin.readline

n = int(input())
col = [0] * n
ans = 0

def attackable(r1, c1, r2, c2):
    if c1 == c2:
        return True
    elif r1-c1 == r2-c2:
        return True
    elif r1+c1 == r2+c2:
        return True
    else:
        return False

def solution(row):
    if row == n:
        global ans
        ans += 1
    else:
        for cand in range(n):
            possible = True
            for i in range(row):
                if attackable(row, cand, i, col[i]):
                    possible = False
                    break

            if possible:
                col[row] = cand
                solution(row+1)
                col[row] = 0

solution(0)
print(ans)