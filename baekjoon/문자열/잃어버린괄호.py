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