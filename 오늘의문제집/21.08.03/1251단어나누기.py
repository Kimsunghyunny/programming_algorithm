import sys
si = sys.stdin.readline

word = si().strip()
word_lst = []
ans = []

for i in range(1,len(word)-1):
    for j in range(i+1,len(word)):
        a, b, c = "".join(reversed(word[0:i])), "".join(reversed(word[i:j])),"".join(reversed(word[j:]))
        ans.append(a+b+c)

ans.sort()
#print(word[0:2][::-1])
print(ans[0])