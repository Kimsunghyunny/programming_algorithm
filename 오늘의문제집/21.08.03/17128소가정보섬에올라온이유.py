import sys
si = sys.stdin.readline

n, q = map(int, si().split())
a = list(map(int, si().split()))
lst = list(map(int, si().split()))

S = 0
for i in range(n):
    S += a[i]*a[(i+1)%n]*a[(i+2)%n]*a[(i+3)%n]

print(S)

for q in lst:
    print("q=",q)
    for i in range(4):
        a[q-1] *= -1
        print(a[q-1])
        S += 2*a[q-1]
        print(S)

    print(S)
