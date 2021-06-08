


n, k = map(int, input().split())
# n과 k 값 받기

c_list = []

for i in range(n):
    c_list.append(i+1)

result = []
popLoca = 0

while len(c_list)>0 :
    popLoca = (popLoca + (k-1)) % len(c_list)
    popVal = c_list.pop(popLoca)
    result.append(str(popVal))

print("<%s>" %(", ".join(result)))
