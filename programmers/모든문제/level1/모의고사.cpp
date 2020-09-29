//완전 탐색

#include <string>
#include <iostream>
#include <vector>
using namespace std;

// 수포자 3인방은 모든 수학 문제를 찍으려 합니다. 1번부터 마지막 문제까지 정답이 순서대로 들은 answer배열이 있을때, 가장 많은 문제를 맞춘 사람이 누구인지 배열에 담에 return 하도록 solution 함수 작성
// 최대 10,000문제로 구성, 문제의 정답은 1~5중 하나,가장 높은 점수를 받은 사람이 여러명일때, 오름차순으로 return.

vector<int> solution(vector<int> answers) {
    vector<int> answer;

    int score[3] = {0};
    int p1[5] = {1,2,3,4,5}, p2[8] = {2,1,2,3,2,4,2,5}, p3[10] = {3,3,1,1,2,2,4,4,5,5};
    
    for( int i =0; i< answers.size(); i++) {
        if(answers[i] == p1[i%5]) score[0]++;
        else if (answers[i] == p2[i%8]) score[1]++;
        else if (answers[i] == p3[i%10]) score[2]++;
    }


// 경우를 나눠야한다. 가장 높은 점수가 있는 사람이 여럿인 경우에는, max값과 비교해서 같을경우에, +1을 하고 없을 경우에는 0으로 초기화해준다.
//ex. 1,2,2인 경우.
    int max = -1;
    int same =-1;
    int same_index[3];
    for (int i=0; i<3; i++) {
        if(max == score[i]){ //중복 높은 값이 있는 경우
            same++;
            same_index[same] = i;
        }
        else if(max<score[i]){ //더 큰 값이 생긴 경우
            same = 0;
            max = score[i];
            same_index[same] = i;
        }
    }

    for(int i=0; i<same+1; i++) {
        answer.push_back(same_index[i]);
    }

    return answer;
}

