

"""

편의점에서 2원 / 5원으로만 거스름돈을 준다.(동전은 무한정 많음)
동전의 개수가 최소가 되도록 거슬러 준다할때, 거스름 돈이 n인 경우, 최소 동전의 개수가 몇 개인지 알려주는 프로그램 작성하기

"""

import sys

input = sys.stdin.readline

n = int(input())

result = 1e9

for i in range(n//5,-1,-1): # 5원짜리로 나눠지는 수에서부터 갯수를 줄여가며 최적의 값 찾기. 
    rest = n - 5*i
    tmp = i
    div = rest % 2
    if div == 0:
        result = min(result, (i+rest//2))
        break # 최소 값이 되기 위해서는 5원짜리를 최대한으로 많이 사용해야하므로. 딱떨어지는 값이 나오는게 가장 빠를수록 가장 최소한의 개수를 사용한것이라 할 수 있다.
    elif tmp == 0: # 5원짜리가 0개이고, 2로 나눠서도 나누어 떨어지지 않으면 거슬러 줄 수 없다는 것이다.
        result = -1

print(result)


