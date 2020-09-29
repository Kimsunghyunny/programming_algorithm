//해시

#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

//{의상이름, 의상부위}로 clothes가 구성되어 있다. 만약 의상 부위가 겹치면 같이 입을 수 없다.
//겹치지 않고 의상 1개 이상을 반드시 입을때 서로 다른 옷의 조합 수를 return.
//clothes에는 {{hat, face}, {blue_shirt, clothes}, {glasses, face}}와 같이 값이 들어가 있다.

int solution(vector<vector<string>> clothes)
{
    int answer = 1;

    unordered_map<string, int> hash_map;
    for (auto a : clothes)
    {
        hash_map[a[1]]++;
    }

    unordered_map<string, int>::iterator tmp; // ** hash테이블과 같은 형태의 iterator로 선언해서 사용
    for (tmp = hash_map.begin(); tmp != hash_map.end(); tmp++)
    {
        answer *= tmp->second + 1;
    }

    return answer - 1;
}