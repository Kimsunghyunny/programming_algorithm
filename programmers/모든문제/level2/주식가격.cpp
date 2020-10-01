#include <string>
#include <vector>
#include <stack>

using namespace std;

/* 주식 가격이 담긴 배열 prices. 가격이 떨어지지 않은 기간은 몇초인지 return.
문제의 의미는, 0초에 1원을 주고 주식을 산 사람이 있을때, 1미만의 가격이 나올때까지의 시간이 얼마나 걸리냐이다.
마찬가지로 1초에 2원 주고 산 사람은 마지막 5초까지 더 싼게 나온게 없으니 3초
2초에 3원주고 산사람은 바로 3초에 2원으로 가격이 내려갔으니 1초.
*/

//스택으로 어떻게 해야할까?
//1,2,3,2,3 으로 들어갔을떄, 4,3,1,1,0으로 return 한다.

vector<int> solution(vector<int> prices)
{
    int size = prices.size();
    vector<int> answer(size);
    stack<int> stack;
    for (int i = 0; i < size; i++)
    {
        while (!stack.empty() && prices[i] < prices[stack.top()])
        {
            answer[stack.top()] = i - stack.top();
            stack.pop();
        }
        stack.push(i);
    }

    while (!stack.empty())
    {
        answer[stack.top()] = size - 1 - stack.top();
        stack.pop();
    }

    return answer;
}
