

# 1번 문제
# https://programmers.co.kr/learn/courses/30/lessons/77486?language=python3

# 풀이 - union-find 알고리즘 사용

def find(parents, money, num, answer):
    # find 함수
    if parents[num] == num or money // 10 == 0:
        answer[num] += money
        return
        
    send = money // 10
    mine = money - send
    answer[num] += mine
    find(parents, send, parents[num], answer)
    return 

def solution(enroll, referral, seller, amount):
    
    # union-find 알고리즘 사용해보기
    n = len(enroll)
    answer = [0] * (n+1)
    d = {}
    parents = [i for i in range(n+1)]
    for i in range(n):
        d[enroll[i]] = i+1
    
    # 추천인 부모 배열에 저장
    for i in range(n):
        if referral[i] == "-":
            parents[i+1] = 0
        else :
            parents[i+1] = d[referral[i]]
    
    # 정산
    for i in range(len(seller)):
        find(parents, amount[i] * 100, d[seller[i]], answer)
        
    return answer[1:]


# enroll : 판매원의 이름
# referral : 다단계 조직에 참여시킨 다른 판매원의 이름을 담은 배열
# seller : 판매량 집계 데이터의 판매원 이름 나열한 배열
# amount : 판매량 집계 데이터의 판매 수량을 나열한 배열
# return : 각 판매원이 득한 이익금을 나열한 배열
#          -> int, enroll의 순서대로 나열









# 2번 문제
#백준 1939번 중량제한 
# https://www.acmicpc.net/problem/1939

# 풀이 - 다익스트라 응용 (최소힙이 아닌 최대힙 사용)
import sys
import heapq
si = sys.stdin.readline

n, m = map(int, si().split())
weight = [0] * (n+1)
edges = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, w = map(int, si().split())
    edges[a].append([w,b])
    edges[b].append([w,a])
s, e = map(int,si().split())

for i in range(1,n+1):
    edges[i].sort(reverse=True)

# 지정된 start 에서의 갈수 있는 각 다리에 대해 최대 중량을 구하기
def solution(start,end):
    q = [[0,start]]
    
    while q:
        w, x = heapq.heappop(q)
        w = -1 * w

        if x == end:
            print(w)
            break

        if weight[x] > w: continue

        for i in edges[x]:
            if w == 0:
                weight[i[1]] = i[0]
                heapq.heappush(q, (-1 * weight[i[1]], i[1]))
            elif weight[i[1]] < i[0] and weight[i[1]] < w:
                weight[i[1]] = min(w, i[0])
                heapq.heappush(q, (-1 * weight[i[1]], i[1]))

solution(s, e)




# 문제 3번
# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
# 문제 풀이 - sliding window 원리 이용, abs 이용

def solution(A):
    part1 = 0
    part2 = sum(A)
    minVal = 1<<31

    for i in range(len(A)-1):
        part1 += A[i]
        part2 -= A[i]
        diff = abs(part1 - part2)
        if minVal == 1<<31:
            minVal = diff
        else:
            minVal = min(diff, minVal)
    
    return minVal
        