

# dfs stack 으로 구현

n = int(input())

#apt = [list(input()) for y in range(n)] 

apt = []
for i in range(n):
    apt.append(list(map(int, input())))


"""
 apt에 대한 정의를 다음과 같이 두가지 방식으로 정의할 수 있다.

 1) apt = [list(input()) for y in range(n)] 

 2) apt = []
    for i in range(n):
    apt.append(list(map(int, input()))) 

** 중요
그러나 여기서 가장 주의해야 할 점은, 1)의 방식은 apt 안의 값이 char의 타입으로 들어가고
 2) 의 방식은 int의 값으로 들어간다는 점이다.
 따라서 만약 if 문에서 1과 비교할지, '1'과 비교할지에 대해서 잘 생각하고
 구현 해야한다는 점에서 주의점이 생긴다. 

"""


stack = []
count = []
tmp = 0

def dfs():
    # 전역변수 n과 tmp를 사용하는 것을 위해  global로 함수 내부에 선언해줌
    global n
    global tmp

    col, row = stack.pop()
    if col >= 0 and row >= 0 and col < n and row < n and apt[col][row] == 1:
        stack.append((col-1,row))
        stack.append((col+1,row))
        stack.append((col,row-1))
        stack.append((col,row+1))
        apt[col][row] = 0
        tmp += 1


for i in range(n):
    for j in range(n):
        if apt[i][j] == 1:
            stack.append((i,j))
            while len(stack) >0 :
                dfs()
            count.append(tmp)
            tmp = 0
                    
print(len(count))
for i in sorted(count):
    print(i)