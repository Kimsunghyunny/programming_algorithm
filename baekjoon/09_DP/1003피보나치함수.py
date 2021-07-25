import sys
si = sys.stdin.readline

T = int(si())
dp1 = [0] * (41)
dp2 = [0] * (41)

def preprocess():
    dp1[0] = 1
    dp2[0] = 0

    dp1[1] = 0
    dp2[1] = 1

    for i in range(2,41):
        dp1[i] = dp1[i-1] + dp1[i-2]
        dp2[i] = dp2[i-1] + dp2[i-2]

preprocess()
for _ in range(T):
    n = int(si())
    print(dp1[n], dp2[n])