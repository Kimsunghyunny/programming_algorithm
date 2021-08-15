

#1. max sliding window

def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
    deque = []
    arr = []

    for i, n in enumerate(nums):

            # k개의 윈도우만 유지 되도록 한다. i가 증가될 때 deque의 0번에 있는 인덱스와 같으면 삭제한다.
            # i - q[0] == k 가 좀 헷갈릴 수 있는데, i, q[0], k 가 각각 3, 0, 3 이라면 아래와 같은 뜻이다.
            # i가 3이면 4번째 인덱스이고 q[0]은 0번째 인덱스이니 유효한 인덱스는 1,2,3 이므로 0번을 삭제하라는 뜻이다.
        if deque and i - deque[0] == k:
            deque.pop(0)

            # nums[i]의 값보다 작은 값들은 모두 삭제한다.
            # 이 과정을 반복함으로써 max값의 후보의 인덱스만 데크에 남게된다.
        while deque and n > nums[deque[-1]]:
            deque.pop()

        deque.append(i)

            # k 번째부터 결과 리스트에 최대값을 넣는다.
        if i >= k - 1:
            arr.append(nums[deque[0]])
    return arr


import collections

def maxSlidingWindow(nums, k):
    results = []
    window = collections.deque()
    current_max = float('-inf') # 시스템이 지정할 수 있는 가장 낮은 값
    for i, v in enumerate(nums):
        window.append(v)
        if i < k - 1:
            continue # 슬라이딩 윈도우 크기보다 작은 경우 pass
        
        # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
        if current_max == float('-inf'):
            current_max = max(window)
        elif v > current_max:
            current_max = v

        results.append(current_max)
        
        # 최댓값이 윈도우에서 빠지면 초기화
        if current_max == window.popleft():
            current_max = float('-inf')
    
    return results


#2. 연속된 k개 요소의 최대 합 구하기(배열의 일정한 범위 1칸씩 미뤄가면서 합꼐 구해서 max와 비교)
def maxSum(arr, n, k):
    if not n > k:
        print("invalid")
        return -1

    max_sum = 0
    window_sum = sum([arr[i] for i in range(k)])
    print(window_sum)

    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(window_sum, max_sum)

    return max_sum

arr = [1,3,7,4,8,4,0, 2]
n = len(arr)
k = 3
print(maxSum(arr, n , k))


#3. k종류의 알파벳으로 이루어진 가장 긴 문자열 길이 찾기
def get_key(dic, val): 
    for key, value in dic.items(): 
         if val == value: 
             return key 
    return "key doesn't exist"


def sliding_window(strs):
    n = len(strs)
    if(n < l): return n
    idx = 0
    ridx, lidx = 0, 0
    maxi = 0
    dic = dict()

    while ridx < n:
        if(len(dic) < k):
            dic[strs[ridx]] = ridx
            ridx += 1
        if(len(dic) == k):
            mini = min(dic.values())
            del dic[get_key(dic, mini)]
            lidx = mini + 1
        maxi = max(maxi, ridx-lidx)

    return maxi

print(sliding_window("ABBBBBBBBBBBCDDDDD"))


#2,3 출처 https://almighty-denver.tistory.com/14?category=903313