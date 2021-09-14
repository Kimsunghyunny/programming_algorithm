import sys
si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))

res = arr[0]
for i in range(1,len(arr)):
    res ^= arr[i]

if res == 0:
    print("cubelover")
else:
    print("koosaga")