
"""

트리에서 리프 노드는 자식의 개수가 0인 노드를 말한다.
트리가 주어졌을 때 노드 하나를 지운다.
그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성해라.
노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.


입력으로 첫째 줄에 노드의 개수 n이 주어진다. n은 50보다 작거나 같은 자연수이다.
둘째 줄에는 0번 노드부터 n-1번 노드까지, 각 노드의 부모가 주어진다. 만약 부모가 없다면(root) -1이 주어진다.
셋째 줄에는 지울 노드의 번호가 주어진다.

출력으로는 셋째 줄에 입력받은 지울 노드를 삭제했을 때의 리프 노드의 개수를 출력한다.

"""

import sys

input = sys.stdin.readline

n = int(input())
#tree = [[] for _ in range(n-1)] 

tree = {} 

lst = list(map(int, input().split()))

dNode = int(input())

for i in range(n):
    if i == dNode or lst[i] == dNode:
        continue
    if lst[i] in tree : # 이미 자식이 1개 이상이 있는 경우 // tree가 dict이기 때문에, key값에 list[i]가 있는지 검사할 수 있다.
        tree[lst[i]].append(i)
    else: # 자식이 아무것도 없는 경우
        tree[lst[i]] = [i]


if -1 in tree:
    q = [-1]
else: # tree에 값이 아예 안들어와서 root가 없는 경우 예외처리
    q = []
ans = 0

while q:
    node = q.pop()
    if node not in tree:
        ans += 1
    else:
        q += tree[node]

print(ans)
