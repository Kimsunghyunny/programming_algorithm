//깊이/너비 우선 탐색

#include <string>
#include <vector>

using namespace std;

//numbers는 사용할 수 있는 숫자가 담긴 배열 target은 numbers을 이용해서 만드려는 숫자
//숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 해라.
//recursion함수를 이용해서 해결하자.

int answer = 0;
void recur(vector<int> numbers, int target, int idx, int sum);

int solution(vector<int> numbers, int target)
{
    recur(numbers, target, 0, 0);
    return answer;
}

void recur(vector<int> numbers, int target, int idx, int sum)
{
    if (idx == numbers.size())
    {
        if (target == sum)
        {
            answer++;
        }
        return;
    }
    recur(numbers, target, idx + 1, sum + numbers[idx]);
    recur(numbers, target, idx + 1, sum - numbers[idx]);
}