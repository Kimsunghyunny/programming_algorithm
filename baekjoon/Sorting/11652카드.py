
import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort() # o(nlogn)

mode = lst[0]
modeCount = 1
curCount = 1

for i in range(1,n):
    if lst[i] == lst[i-1]:
        curCount +=1
    else:
        curCount = 1
    if curCount > modeCount:
        mode = lst[i]
        modeCount = curCount    

print(mode)