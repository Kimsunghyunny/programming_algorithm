import sys
si = sys.stdin.readline


ans = []
while True:
    n, k = map(int, si().split())
    if n == 0 and k == 0:
        break

    g = list(map(int, si().split()))
    level = [[] for _ in range(20)]
    levelval = [-1] * 20 # 해당 레벨에 몇개의 원소가 존재하는지 count
    # level 별로 넣어둘 수 있는 배열을 하나 만들고, k의 레벨을 구한뒤에 k 레벨 배열의 길이 - 1을 해준다.
    ansLevel = 0
    cnt = -1

    
    for i in range(1,n):
        if g[i] == k:
            ansLevel = cnt
        if g[i] != g[i-1] + 1:
            cnt += 1
        levelval[i] = cnt

    print(levelval)
    print(ansLevel)

    ans = 0
    for i in range(1, n+1):
        if levelval[i] != levelval[ansLevel] and levelval[levelval[i]] == levelval[levelval[ansLevel]]:
            ans += 1
    print(ans)
    

        