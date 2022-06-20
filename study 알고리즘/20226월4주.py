
'''
문제 1번 - 프로그래머스 입국심사 lv3 https://programmers.co.kr/learn/courses/30/lessons/43238
풀이 방법 : 이분탐색
시간 복잡도 : o(logN) -> 16,000 * 2 
'''
def solution(n, times):
    
    l, r = 1, n * max(times)
    res = 0
    
    while l <= r:
        mid = (l+r)//2
        cnt = 0
        for t in times:
            cnt += mid // t
            if cnt >= n:
                break
                
        if cnt >= n:
            res = mid
            r = mid - 1
        else :
            l = mid + 1
            
    return res

'''
*문제 요약
한 심사대에서는 동시에 한명만 심사 가능.
가장 앞에 서 있는 사람은 비어있는 심사대로 가서 심사받음
모든 사람이 심사를 받는데 걸리는 시간을 최소로

임국 심사를 기다리는 사람수 n
각 심사관이 한명을 심사하는데 걸리는 시간이 담긴 배열 times

--> 모든 사람이 심사를 받는데 걸리는 시간의 최솟값

1명 <= n <= 1,000,000,000명
1분 <= t <= 1,000,000,000분
1명 <= m <= 100,000명 (심사관)

---------------------------------------------------------------------------------------------------

1. 풀이할 수 있는 방법은?
- 완전 탐색이나, 이진탐색?
- 가장 max로 걸리는 시간은 얼마일까?
모든 사람이 times중에서 심사하는데 가장 오래걸리는 심사관한테 가서 받기위해서 계속 대기하고 심사하는 경우가 가장 최악의 경우가 될것


2. 시간 복잡도는?
- 완전탐색으로 풀이시,
n이 10억명까지 올 수 있으므로, 1초 시간내에 불가능.
- 이진탐색으로 풀이시,
o(logN)이므로, 최소(1)~최대(10억^2) 이므로 약 16000 * 2 이므로, 1초이내에 풀이가능


3. 이분탐색으로 풀이를 위한 준비
- sort
해당 문제는 sort없이 최소, 최대 시간을 구해 구간을 탐색하는 것이므로,
sorting이 필요하지 않다.
'''




'''
문제 2번 - 구간 나누기 2 https://www.acmicpc.net/problem/13397
풀이 방법 : 이분탐색
시간 복잡도 : o(logN)

1<= N <= 5,000
1<= M <= N
1<= N[x] <= 10,000

풀긴 하는데,, 풀다보면 갑자기 헷갈림 
'''
import sys
si = sys.stdin.readline

n, m = map(int, si().split())
lst = list(map(int, si().split()))

# 구간을 나누고 최대-최소의 최소값이 mid 값 기준에 맞게 
def sol(mid):
    # 구간에서의 min, max 값
    minVal, maxVal = lst[0], lst[0]
    # 구간의 개수 cnt
    cnt = 1

    for i in range(1,n):
        minVal = min(minVal, lst[i])
        maxVal = max(maxVal, lst[i])
        # max - min 이 최대값중의 최소값보다 크면 새로운 구간이 만들어져야함
        if maxVal - minVal > mid:
            cnt += 1
            minVal = lst[i]
            maxVal = lst[i]
    return m >= cnt

# 최대값중에서 최소값은 lst의 가장 큰 값보다 작거나 같게 나올수밖에 없고, 최소값의 가장 작은 값을 0
l, r = 0, max(lst)
res = 1<<31

while l <= r:
    # mid = 최대값중에서 최소값
    mid = (l+r)//2
    if sol(mid): # 구간의 수가 m 이하인경우
        res = min(res, mid)
        r = mid - 1
    else: # 구간의 수가 m 초과인 경우
        l = mid + 1


print(res)

'''
8 3
1 5 4 6 2 1 3 7
'''



'''
문제 3번 - MinMaxDivision https://app.codility.com/programmers/lessons/14-binary_search_algorithm/min_max_division/
풀이 방법 : 이분탐색
시간 복잡도 : o(logN)
'''

def solution(K, M, A):
    l, r = 0, M * len(A)
    res = 1<<31
    while l <= r:
        mid = (l+r)//2
        sum = 0
        maxSum = 0
        cnt = 1

        for i in A:
            if sum + i > mid:
                maxSum = max(sum, maxSum)
                sum = i
                cnt += 1
            else:
                sum += i
        maxSum = max(sum,maxSum)
        if cnt <= K:
            r = mid - 1
            res = min(maxSum, res)
        else:
            l = mid + 1
    return res