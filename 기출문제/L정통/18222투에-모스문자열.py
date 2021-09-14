import sys
si = sys.stdin.readline

n = int(si())

def recur(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    if k % 2:
        return 1 - recur(k//2)
    else:
        return recur(k//2)

print(recur(n-1))


