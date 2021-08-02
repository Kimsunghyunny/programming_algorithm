import sys
si = sys.stdin.readline

n, m = map(int, si().split())
time = list(map(int, si().split()))

#완전탐색은 시간초과이니 탐색을 빠르게 할 수 있는 이분탐색을 고려해보자.
t = 0
if n <= m:
    print(n)
else: # 이분탐색으로 아이들을 모두 태울 수 있는 시간을 찾기
    l, r = 0, 10**20
    cnt = 0
    while l <= r:
        mid = (l+r)//2
        cnt = m # 처음0초에는 모두가 탑승하기 때문에
        for i in range(m):
            cnt += mid // time[i]
        if cnt >= n:
            t = mid
            r = mid - 1
        else:
            l = mid + 1
    # 위 코드를 통해 마지막 탑승인원까지 포함할 수 있는 가장 최소의 시간을 구하게 된다.
    s = m
    for i in range(m):
        s += (t-1)//time[i] # 마지막 탑승자 직전시간에 해당 놀이기구 탔던 사람의 수 
    for i in range(m):
        if t % time[i] == 0: # 시간이 딱 떨어지는 시간들에 1명씩 더 탈 수 있기에 s에 1더해주기
            s += 1
        if s == n:
            print(i+1)
            break