//완전탐색

#include <string>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

//한자리 숫자가 적힌 종이 조각. 이 종이 조각들을 붙여 소수를 몇 개 만들 수 있는지?
//각 종이에 적힌 숫자 배열 numbers. 
//numbers는 1~7개 사이. 

// 소수의 조건? 자기 자신과 1로만 나눌 수 있는 숫자. --> 제곱근 값 이하까지만 나눠보자.

int solution(string numbers) {
    int answer = 0;


    // numbers에 들어온 숫자로 다양한 숫자 합 만들어보기.
    //ex. 178이 들어올 경우, 3*2*1 = 6가지.(178,187, 718,781, 817,871)가 발생할 수 있다. 단, 0이 들어올 경우에는 ex. 013은 2*2*1 = 4가지. (103, 130, 301, 310)

    vector<int> case; //발생할 수 있는 숫자들의 목록

//알고리즘 좀더 생각해보기.    

    return answer;
}