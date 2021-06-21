
import sys

input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    tmpLst = []
    for j in range(1,len(tmp)):
        if tmp[j] == -1:
            break
        else:
            tmpLst.append(tmp[j])
    lst.append([tmp[0], tmpLst])
    #print(lst)

root = int(input())

for i in range(n):
    if lst[i][1] == [root]:
        lst[i][1].remove(root)
        if lst[i][1] == []:
            lst[i].pop()


# root부터 차례대로 정렬하기
