


"""


시간초과 dp의 방법

import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)
dp[0], dp[1] = 0, 1

for i in range(2,n+1):
    if (i**0.5).is_integer():
        dp[i] = 1
    else:
        dp[i] = i

for i in range(2, n+1):
    for j in range(1, int(i**0.5)+1):
        dp[i] = min(dp[i], dp[j*j]+dp[i-j*j])

print(dp[n])


"""


import sys

input = sys.stdin.readline
n = int(input())

def four_squares(n):
    if (n ** 0.5).is_integer():
        return 1
    for i in range(1, int(n ** 0.5) + 1):
        if n < i ** 2:
            break
        if ((n - i ** 2) ** 0.5).is_integer():
            return 2
    for i in range(1, int(n**0.5) + 1):
        if n < i ** 2:
            break
        for j in range(1, int((n - i ** 2) ** 0.5) + 1):
            if n < i ** 2 + j ** 2:
                break
            if ((n - i ** 2 - j ** 2) ** 0.5).is_integer():
                return 3
    return 4

print(four_squares(n))