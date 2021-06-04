

# dfs stack 으로 구현

n = int(input())

apt = []

for i in range(n):
    apt.append(list(map(int, input())))

stack = []
count = []
tmp = 0

def dfs():
    global n
    global tmp

    x, y = stack.pop()
    if y >= 0 and x >= 0 and y < n and x < n and apt[x][y] == '1':
        stack.append((x-1,y))
        stack.append((x,y+1))
        stack.append((x+1,y))
        stack.append((x,y-1))
        apt[x][y] = '0'
        tmp += 1



for i in range(n):
    for j in range(n):
        if apt[i][j] == '1':
            stack.append((i,j))
            while len(stack) >0 :
                dfs()
            count.append(tmp)
            tmp = 0


print(len(count))
for i in sorted(count):
    print(i)