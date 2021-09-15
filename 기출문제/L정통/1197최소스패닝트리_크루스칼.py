import sys
si = sys.stdin.readline

def find(x):
    global parent

    if parent[x] == x:
        return x
    else:
        return find(parent[x])

def union(x,y):
    print("uisniot")
    pX, pY = find(x), find(y)
    if pX > pY:
        parent[pX] = pY
    else:
        parent[pY] = pX
    print(parent)

v, e = map(int, si().strip().split())
arr, parent = [], [i for i in range(v)]
for _ in range(e):
    v1, v2, dist = map(int, si().strip().split())
    arr.append([dist, v1-1, v2-1])
arr.sort()

res = 0
for a in arr:
    print(a)
    if find(a[1]) == find(a[2]):
        continue

    union(a[1],a[2])
    res += a[0]
print(res)