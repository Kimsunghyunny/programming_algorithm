

import sys

input = sys.stdin.readline

N = int(input())

cardLst = []

for _ in range(N):
    cardLst.append(int(input()))

cardLst.sort()

# 2개를 더할때, 그 상황에서 가장 작은 값이 나오도록 더해준다.

