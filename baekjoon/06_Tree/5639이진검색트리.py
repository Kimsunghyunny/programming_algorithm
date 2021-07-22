

import sys
si = sys.stdin.readline
sys.setrecursionlimit(10**9)

# 입력으로 트리를 전위순회한 결과가 주어진다. 

tree = []
cnt = 0

def dfs(start, end):
    if start > end:
        return
    div = end + 1
    for i in range(start + 1, end + 1):
        if tree[start] < tree[i]:
            div = i
            break
    
    dfs(start + 1, div - 1)
    dfs(div, end)
    print(tree[start])

    

while cnt <= 10000:
    try:
        x = int(si())
    except:
        break
    tree.append(x)
    cnt += 1

dfs(0, len(tree) - 1)