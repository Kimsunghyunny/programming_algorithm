import sys
si = sys.stdin.readline

n = int(si())
a = []

for i in range(n):
    x = si()
    a.append((x,len(x)))

#중복삭제
a = list(set(a))

#정렬
a.sort(key = lambda w: (w[1],w[0]))

for w in a:
    print(w[0],end='')