
"""
 루트 없는 트리가 주어질때, 트리의 루트를 1이라 정했을때, 각 노드의 부모를 구하는 프로그램을 작성

첫째 줄에 노드의 개수 n(2 <= n <= 100,000)이 주어진다.
둘째 줄부터 n-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력으로는 n-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

이진트리의 경우에는 연산에 대한 시간복잡도가 o(n)이다.

"""



import sys

input = sys.stdin.readline

n = int(input())

tree = [[]for i in range(n+1)]
# 0부터 n까지의 일차배열 여러개를 생성한다. 즉, list를 가진 배열으로 만든다.
# tree[0] = {1,2,3}, tree[1] = {4,5,6} 이런식으로 되어 있는 형태라고 볼 수 있다.
#https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=wjddudwo209&logNo=221253421426 참고

for i in range(n-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    # a,b를 이중으로 연결해준다.

q = [1] # 큐에 1값을 넣어둔다.
ans = {} # dict으로 선언해서 사용. []로 선언해 배열을 이용하면 ans[i]에 값을 넣으려 할때 outboud of index 에러가 발생한다.
#만약 배열로 사용하고 싶다면 배열로 ans = [0] * (n+1) 로 초기화를 선언해줘야한다.
check = [False for _ in range(n+1)] # 방문여부를 확인하는 배열을 선언

while len(q)>0 :
    parent = q.pop(0) #0번째 값 pop하기 시간복잡도 o(1)이다.
    for i in tree[parent]: # tree[1] = {4,6}
        if not check[i]:
            ans[i] = parent
            q.append(i)
            check[i] = True # i번째 들에대해서는 방문 여부를 표시해 이미 방문해서 기입한 부분에 대해서는 다시 기입 하지 않도록 한다.


for i in range(2, n+1):
    print(ans[i])
    # dict에서 value값 출력
