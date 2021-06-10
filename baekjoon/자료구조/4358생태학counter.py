import sys
from collections import Counter

trees=Counter(sys.stdin.readline().split('\n')[:-1])
# split뒤에 [:-1]을 작성한 이유는, counter 같은경우에는 잘라진 것의 갯수를 세는것인데, 잘라진 단어에서 0부터 -2까지의 범위를 정해준것이라 보면 된다.
# 즉, \n을 기준으로 자른 다음에 \n을 포함하지 않고 단어를 저장해 카운팅하는 것이라 생각하면 된다.

N=sum(list(trees.values()))

for key in sorted(trees.keys()):
    print(key,"%.4f"%(trees[key]/N*100))