"""

첫 줄에 테스트 케이스의 개수 T가 주어집니다.

각 테스트 케이스마다, 첫째 줄에 트리를 구성하는 노드의 수 N이 주어집니다. (2 ≤ N ≤ 10,000)

그리고 그 다음 N-1개의 줄에 트리를 구성하는 간선 정보가 주어집니다. 

한 간선 당 한 줄에 두 개의 숫자 A B 가 순서대로 주어지는데, 이는 A가 B의 부모라는 뜻입니다. 

(당연히 정점이 N개인 트리는 항상 N-1개의 간선으로 이루어집니다!) A와 B는 1 이상 N 이하의 정수로 이름 붙여집니다.

테스트 케이스의 마지막 줄에 가장 가까운 공통 조상을 구할 두 노드가 주어집니다.

"""


# --> 최소공통조상 알고리즘을 이용한다.
# https://developmentdiary.tistory.com/467 참고.


import sys

input = sys.stdin.readline

test = int(input())

ans = []

for _ in range(test):
    n = int(input()) # 트리를 구성하는 노드의 수
    treeMap = [0 for _ in range(n+1)]

    for i in range(n-1):
        a, b = map(int, input().split())
        treeMap[b] = a

    c, d = map(int, input().split())

    c_list = [c]
    d_list = [d]

    while treeMap[c]:
        c_list.append(treeMap[c])
        c = treeMap[c]

    while treeMap[d]:
        d_list.append(treeMap[d])
        d = treeMap[d]

    
    c_level = len(c_list)-1
    d_level = len(d_list)-1

    while c_list[c_level] == d_list[d_level] :
        c_level -= 1
        d_level -= 1
    
    ans.append(c_list[c_level+1])

for _ in range(len(ans)):
    print(ans[_])
