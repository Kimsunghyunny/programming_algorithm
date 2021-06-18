import sys
input = sys.stdin.readline

N = int(input())
postOffice = [list(map(int, input().split())) for _ in range(N)]

postOffice.sort(key=lambda x: x[0])
mid = round(sum(p for _, p in postOffice)/2) # round를 이용해 반올림하자. 

pCount = 0
for i, p in postOffice:
    pCount += p

    if pCount >= mid:
        print(i)
        break

# 우체국을 건설하기 위한 위치는 인구수대로 정렬하여 인구의 절반 이상이 되는 순간 그 위치에 우체국을 지어야하는 방법이다.
 