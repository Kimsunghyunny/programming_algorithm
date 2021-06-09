
""" 
1<= n <= 10,000 
1<= m <= 10,000
--> n과 m에 대해서 최대 값인 10,000끼리 무작정 for문을 돌리면 시간초과가 발생한다.
따라서 이에 대해서는 올바른 자료구조를 이용해서 시간초과 없이 구현할 수 있도록 해야한다.

딕셔너리와 트라이 구조를 사용하는 것으로 생각해보자.

1) 딕셔너리 방법
n개의 문자열을 입력받아 딕셔너리에 저장하고 이후 M개의 문자열을 입력받을 때마다 딕셔너리에 존재하는지 찾는다.
여기서 딕셔너리를 사용하는 이유는 탐색과정에서 O(1)의 시간 복잡도를 가지기 때문이다.
list를 사용하는 경우에는 특정 값이 있는지 검색하기 위해 O(n)의 시간 복잡도를 가지기에 시간초과할 확률이 높다.
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))

nDic = dict()
ans= 0;

for _ in range(n):
    nWord = input()
    nDic[nWord] = True

for _ in range(m):
    mWord = input()

    if mWord in nDic.keys():
        ans += 1
    
print(ans)