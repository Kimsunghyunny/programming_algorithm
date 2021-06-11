

"""

1. python 배열의 선언


"""

1-0) dp = [0]*n

0 0 0 0 0 0 0 ... n-1 로 되어있는 일차원 배열 선언
dp[0] = 1 이면 1 0 0 0 0 0 0 ... n-1 로 바뀐다. (그러나 이차원 배열은 위와 같이 선언하면 안된다.)



1-1) dp = [[]] * 10

10개의 [](list)들이 모두 1개의 메모리를 가리키고 있기 때문에 
dp[0].append(1)을 하면 0부터 9번까지 모든 10개의 list에 값이 1이 들어가게된다.



1-2) dp = [[] for _ in range(10)]

10개의 [](list)들이 모두 다른 메모리를 가리키고 있기 때문에
dp[0].appned(1), dp[0].append(2), dp[1].append(4) 를하면
dp[0] = {1,2} dp[1] = {4} 와 같이 들어가게된다.

https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=wjddudwo209&logNo=221253421426 참고하기



1-3) dp =[[0]*n for _ in range(m)]

n개의 0으로 형성된 리스트를 m줄을 만든다는 의미이다. 즉 이차원배열이라 생각하면 된다.
즉, { 0, 0, 0, 0, 0, ... n-1} 형태의 리스트가 m줄 있다는 의미이다.
만약 이러한 이차원 배열을 dp=[[0]*n]*m으로 선언하면 m개의 [0]*n이 모두 같은 객체로 인식되기 때문에 dp[0][0] =1 로 바꾸면
dp[0~n-1][0]은 모두 1로 바뀌게 된다.




"""

2. python 값 한번에 여러개 입력받기

"""

a,b = map(int, input().split())
' '을 기준으로 잘라서 int로 바꿔 a,b에 저장한다





"""

3. () [] {} 의 차이

"""

https://hashcode.co.kr/questions/4118/의-차이와-사용해야-할-곳 참고



3-1) Array

array는 []를 쓰는 대표적인 타입이다.
[]는 배열을 선언 & 초기화 할때 배열의 원소에 접근할 때 사용한다.
array는 ()나 {}를 사용하지 않는다.

arr = []
arr = [1,2,3,4]
arr[3] 3번째 원소에 접근



3-2) tuple

tuple은 ()를 쓰는 대표적인 타입니다.
()는 튜플을 선언 & 초기화할때 사용한다.
[]는 튜플의 원소에 접근할 때사용한다. {}는 사용하지 않는다.

mytuple = ()
mytuple = (1,2,3,4)
mytuple[3] 3번째 원소에 접근



3-3) Dictionary

dictionary는 {}를 쓰는 대표적인 타입인디ㅏ. {}는 딕셔너리를 선언&초기화 할때 사용합니다.
[]는 key에 대응하는 value를 할당하거나 value에 접근할 때 사용한다.

mydict = {}
mydict = {"m":3, "p":5}
mydict["m"]
mydict["c"] = 1 ß



"""

기타 

"""


if __name__ == "__main__":
이와 같은 것은 여러 클래스 파일을 포함하고 있는경우에, 해당 코드가 적혀 있는 파일이 main으로 실행되었을 때 
아래의 코드가 실행된다는 의미를 담고 있다.
