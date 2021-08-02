import sys
si = sys.stdin.readline

# 연속된 글자의 부분집합이 맞는지 아닌지 찾기 -> 투포인터!?
s = si().strip()
p = si().strip()
cnt = 0

def twopointer(l, r):
    global cnt
    while l < r:
        if s[l] == p[cnt]:
             cnt += 1
             l += 1
        if s[r] == p[-(len(p)-cnt)]:
            cnt += 1
            r -= 1

        if cnt == len(p):
            return True
    return False

for i in range(len(s)):
    cnt = 0
    if s[i] == p[cnt]:
        cnt += 1
        # 투포인터 탐색
        if twopointer(i+1,i+(len(p)-1)):
            print(1)
        else:
            print(0)
# 위의 투포인터는 그냥 완전탐색과 시간복잡도가 같다. 그렇기에 문자열 길이가 100만 미만인 경우에는 당연히 시간이 초과할 수 밖에 없다.


"""
아래는 kmp 코드

def getPI(pattern):
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

def KMP(s, pattern):
    getPI(pattern)
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != pattern[j]:
            j = pi[j - 1]
        if s[i] == pattern[j]:
            if j == len(pattern) - 1:
                return True
            else:
                j += 1
    return False

s = input()
pattern = input()
pi = [0 for x in range(len(pattern))]

if KMP(s, pattern):
    print('1')
else:
    print('0')


"""

