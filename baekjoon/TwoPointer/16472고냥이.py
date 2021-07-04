import sys
input = sys.stdin.readline

n = int(input())
lst = input().strip()
cnt = [0] * 26
kind = 0

l, ans = 0, 0


def add(x):
    global cnt
    global kind
    val = ord(x) - ord('a')
    cnt[val] += 1
    if cnt[val] == 1:
        kind += 1


def erase(x):
    global cnt
    global kind
    val = ord(x) - ord('a')
    cnt[val] -= 1
    if cnt[val] == 0:
        kind -= 1


for r in range(len(lst)):

    add(lst[r])

    while kind >n:
        erase(lst[l])
        l+=1
    ans = max(ans, r-l+1)

print(ans)