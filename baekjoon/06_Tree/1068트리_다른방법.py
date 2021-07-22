



#내가 원하는 방법으로 구현한 방법

import sys
input=sys.stdin.readline


N=int(input())
nodes=[[] for  i in range(N)] # 초기화

for idx,p in enumerate(map(int,input().split())):
	if p==-1: continue
	nodes[p].append(idx) # nodes 배열에서 p를 부모로 하는 자식들의 값을 넣어준다.
print()
for i in nodes:
    print("node값 출력",i)

rem=int(input())

def remove(rem):
	for i in nodes[rem]: # 지우려는 노드의 자식들과 해당 자식들의 자식들까지 모두 none으로 만들어 주는 함수
		remove(i)
	nodes[rem]=None


remove(rem)

for idx, i in enumerate(nodes):
    #if i in ([], [rem]): # 노드의 자식이 []로 빈칸이거나, 
        print(idx, ':', i)

print(sum([1 if i in([],[rem]) else 0 for i in nodes]))

"""
# sum (
    for i in nodes
        if i in ([], [rem]):
            1
        else
            0
    )
을 한줄로 작성한 것이다.
"""