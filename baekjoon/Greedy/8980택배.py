
import sys

input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())

post = [list(map(int, input().split())) for _ in range(M)]
post.sort(key=lambda x: x[1])

on = [0] * (N+1)

sumVal = 0
ans = 0

for i in range(1,N+1):
    ans += on[i]
    sumVal -= on[i]
    on[i] = 0
    for _, b, c in post:
        if sumVal + c <= M:
            sumVal += c
            on[b] += c
        else:



#https://www.acmicpc.net/source/17909140 해당 코드 이해하기