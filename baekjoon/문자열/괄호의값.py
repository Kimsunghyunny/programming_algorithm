import sys
si = sys.stdin.readline

lst = si()
stack = []
ans = 0
tmp = 1

for i in range(len(lst)-1):
    if lst[i] == '(':
        stack.append(lst[i])
        tmp *= 2
    elif lst[i] == '[':
        stack.append(lst[i])
        tmp *= 3
    elif lst[i] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if lst[i-1] == '(':
            ans += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if lst[i-1] == '[':
            ans += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(ans)