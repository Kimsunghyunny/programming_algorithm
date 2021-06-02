

def star(n):
    global Map

    if n == 3:
        Map[0][:3] = Map[2][:3] = [1]*3
        Map[1][0] = Map[1][2] = 1
        return

    a = int(n/3) # python에서는 정수/정수 해도 float이 나오니, 정수 값을 원하면 int함수를 이용하거나 //을 이용하자
    star(a)
    for i in range(3) :
        for j in range(3) :
            if i == 1 and j == 1 :
                continue
            for k in range(a) :
                Map[a*i+k][a*j:a*(j+1)] = Map[k][:a]
        

N = int(input())

Map = [[0 for i in range(N)] for i in range(N)] # N*N 이차원 배열 초기화

star(N) # star 함수 실행

for i in Map :
    for j in i :
        if j :
            print('*', end = '')
        else :
            print(' ', end = '')
    print()

#