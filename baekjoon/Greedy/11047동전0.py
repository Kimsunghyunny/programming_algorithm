
"""

준규가 가지고 있는 동전은 총 n종류이고, 각각의 동전을 매무 많이 갖고 있다.
동전을 적절히 사용해 그 가치의 합을 k로 만드려고 할때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성

1<=N<=10, 1<=K<=100,000,000

"""


import sys

input = sys.stdin.readline

n, k = map(int,input().split())

lst = []

for _ in range(n):
    lst.append(int(input()))

result = 0

lst.sort(reverse=True)

for i in lst:
    if k == 0:
        break;
    tmp = k // i
    k -= tmp * i
    result += tmp 

print(result)
