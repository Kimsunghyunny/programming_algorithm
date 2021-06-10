"""
미국 전역의 나무들이 주어졌을 때, 각 종이 전체에서 몇 %를 차지하는지 구하는 프로그램

입력으로는 한줄에 하나의 나무 종 이름이 주어진다.
어떤 종 이름도 30글자를 넘지 않는다.
입력에는 최대 10,000개의 종과 최대 1,000,000그루의 나무가 주어진다.

출력으로는 각 종의 이름을 사전순으로 출력하고, 그 종이 차지하는 비율을 백분율로 소수점 4째자리까지 반올힘해 함께 출력
"""

import sys

input = sys.stdin.readline
trees = dict()
total = 0

while True:
    newTree = input().rstrip() # 오른쪽의 \n 삭제해주기
    if not newTree:
        break
    if newTree in trees:
        trees[newTree] += 1
    else:
        trees[newTree] = 1
    total += 1

treesLst = list(trees.keys())
treesLst.sort()
for tree in treesLst:
    sys.stdout.write('%s %.4f\n' %(tree, trees[tree]/total*100))

