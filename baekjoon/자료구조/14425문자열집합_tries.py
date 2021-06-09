""" 
1<= n <= 10,000 
1<= m <= 10,000
--> n과 m에 대해서 최대 값인 10,000끼리 무작정 for문을 돌리면 시간초과가 발생한다.
따라서 이에 대해서는 올바른 자료구조를 이용해서 시간초과 없이 구현할 수 있도록 해야한다.

딕셔너리와 트라이 구조를 사용하는 것으로 생각해보자.

2) 트라이 구조 
탐색 속도는 딕셔너리 방법이 훨씬 빠르지만, 트라이 구조도 list보다 빠르기 때문에 사용할 수 있다.
트라이 구조는 O(L)의 시간복잡도를 가지는데, 여기서 L은 가장 긴 문자열의 길이로 이 문제에서는 개수가 10,000이지만 문자열의 최대 길이는 500이므로
list보다 훨씬 빠르다는 것을 알 수 있다. 
"""

import sys

input = sys.stdin.readline

class Node:
    def __init__(self, key):
        self.key = key
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]
        cur.child['*'] = True
    
    def search(self,word):
        cur = self.head

        for ch in word:
            if ch not in cur.child:
                return False
            cur = cur.child[ch]
        if '*' in cur.child:
            return True

n, m = map(int, input().split())
trie = Trie()
ans = 0

for _ in range(n):
    s = input()
    trie.insert(s)

for _ in range(m):
    candi = input()
    
    if trie.search(candi):
        ans += 1

print(ans)