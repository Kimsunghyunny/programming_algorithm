import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
visit = [0] * (n+1)

#인접행렬 만들기
a = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x) # 방향이 없음에도 이와 같이 서로 연결을 해줘야 한다. 이 코드가 없으면 틀린 예외가 생겨서 x.
    # 가령, 값중 x,y 서로 교차해서 저장하지 않는다면, dfs의 재귀 순서에 따라 어떤 떄는 맞고 어떤 때는 틀린 답이 나올 수 있기 때문에 교차 저장해주는 것이 좋다.

def dfs(x):
    visit[x] = 1
    
    for y in a[x]:
        if visit[y]: continue
        dfs(y)

cnt = 0
for i in range(1,n+1):
    if visit[i]: continue
    dfs(i)
    cnt +=1

print(cnt)