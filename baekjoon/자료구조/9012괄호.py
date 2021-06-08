
n = int(input())
ck = True

def check(string):
    global ck
    stack = []
    
    ck = True
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(i)
        elif string[i] == ')':
            if stack:
                stack.pop()
            else:
                ck = False
    if ck == False or stack:
        print("NO")
    else:
        print("YES")


for i in range(n):
    string = input()
    check(string)
    