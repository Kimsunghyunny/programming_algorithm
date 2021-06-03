

def star(n):
    global Map

    if n == 3:
        Map[0][:3] = Map[2][:3] = [1]*3
        Map[1][0] = Map[1][2] = 1
        return # return을 하지 않으면 recursion 에러가 발생한다. 
        #python에서 정의한것보다 재귀가 더 깊게 들어가 생기는 오류로 , 끝이나지 않기 때문에 발생하는것같다.

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