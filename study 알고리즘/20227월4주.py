# 백준
# 잃어버린 괄호 https://www.acmicpc.net/problem/1541

import sys
si = sys.stdin.readline

val = si().split("-")
ans = 0
nums = []
for i in val:
    tmp = i.split("+")
    sum = 0
    for j in tmp:
        sum += int(j)
    nums.append(sum)

ans = 0

for i in range(len(nums)):
    if i == 0:
        ans = nums[i]
    else:
        ans -= nums[i]

print(ans)



# 백준
# 괄호의 값 https://www.acmicpc.net/problem/2504
import sys
si = sys.stdin.readline

lst = si()
stack = []
ans = 0
tmp = 1

for i in range(len(lst)-1):
    if lst[i] == '(':
        stack.append(lst[i])
        tmp *= 2
    elif lst[i] == '[':
        stack.append(lst[i])
        tmp *= 3
    elif lst[i] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if lst[i-1] == '(':
            ans += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if lst[i-1] == '[':
            ans += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(ans)


# 백준
# 두 용액 https://www.acmicpc.net/problem/2470

import sys
import math
si = sys.stdin.readline

n = int(si())
lst = list(map(int, si().split()))
lst.sort()

l, r = 0, n-1
bestSum = 1<<31
v1, v2 = 0, 0

while l < r:
    sum = lst[l] + lst[r]
    if bestSum > abs(sum):
        v1 = lst[l]
        v2 = lst[r]
        bestSum = abs(sum)

    if sum < 0:
        l += 1
    else:
        r -= 1

print(v1, v2, " ")


# 백준
# 세 용액 https://www.acmicpc.net/problem/2473
import sys
si = sys.stdin.readline

n = int(si())
lst = list(map(int, si().split()))
lst.sort()

v1, v2, v3 = 0, 0, 0
bestSum = 3*(10**9)  # long으로 선언 x시 틀림
flag = 0
for i in range(n-2):
    l, r = i+1, n-1
    while l < r:
        nowSum = lst[i] + lst[l] + lst[r]
        if bestSum > abs(nowSum):
            bestSum = abs(nowSum)
            v1 = lst[i]
            v2 = lst[l]
            v3 = lst[r]
        if nowSum > 0: r-=1
        elif nowSum < 0 : l+=1
        else: 
            flag = 1
            break

    if flag : break

print(v1, v2, v3) 