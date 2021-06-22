
import sys
input = sys.stdin.readline

n = int(input())

def solution():
    coinN = int(input())
    coinKind = list(map(int, input().split()))
    result = int(input())

    dp = [0] * (result + 1)

    dp[0] = 1
    for coin in coinKind:
        for i in range(coin,result+1):
            dp[i] += dp[i-coin]
    
    return dp[result]


if __name__ == "__main__":    
    for _ in range(n):
        solution()
