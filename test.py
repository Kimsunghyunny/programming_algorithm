
#중복 허용해서 순서있게 나열
import sys
n, m = map(int, sys.stdin.readline().split(' '))

selected = [0 for _ in range(m)]
used = [0 for _ in range(n + 1)]
def rec_func(k):
    if k == m:
        for x in selected:
            sys.stdout.write(str(x) + ' ')
        sys.stdout.write('\n')
    else:
        for cand in range(1, n + 1):
            selected[k] = cand
            rec_func(k + 1)
            selected[k] = 0

rec_func(0)



# 중복 없이 순서있게 나열
import sys
n, m = map(int, sys.stdin.readline().split(' '))

selected = [0 for _ in range(m)]
used = [0 for _ in range(n + 1)]
def rec_func(k):
    if k == m:
        for x in selected:
            sys.stdout.write(str(x) + ' ')
        sys.stdout.write('\n')
    else:
        for cand in range(1, n + 1):
            if used[cand]:
                continue
            selected[k] = cand
            used[cand] = 1
            rec_func(k + 1)
            selected[k] = 0
            used[cand] = 0

rec_func(0)



# 중복 허용해서 고르기
import sys
n, m = map(int, sys.stdin.readline().split(' '))

selected = [0 for _ in range(m)]
used = [0 for _ in range(n + 1)]
def rec_func(k):
    if k == m:
        for x in selected:
            sys.stdout.write(str(x) + ' ')
        sys.stdout.write('\n')
    else:
        start = 1 if k == 0 else selected[k - 1]
        print("start =",start)
        for cand in range(start, n + 1): # 순서 있게 나열이랑 다르게 start를 지정해준다.
            selected[k] = cand
            rec_func(k + 1)
            selected[k] = 0

rec_func(0)


# 중복없이 고르기
import sys
n, m = map(int, sys.stdin.readline().split(' '))

selected = [0 for _ in range(m)]
used = [0 for _ in range(n + 1)]
def rec_func(k):
    if k == m:
        for x in selected:
            sys.stdout.write(str(x) + ' ')
        sys.stdout.write('\n')
    else:
        start = 1 if k == 0 else selected[k - 1] + 1
        for cand in range(start, n + 1):
            selected[k] = cand
            rec_func(k + 1)
            selected[k] = 0

rec_func(0)
