//해시

#include <iostream>
#include <string>
#include <vector>
#include <unordered_map> 

using namespace std;


//마라톤에 참여한 선수들의 이름이 담긴 participant 배열과 완주한 선수들이 담긴 completion 배열이 주어질때, 
// 완주하지 못한 선수들의 이름을 return 해라.

//경기에 참여한 선수는 1~100,000명
//completion의 길이는 participant의 길이보다 1작다
//참가자의 이름은 1~20개의 알파벳 소문자
//동명이인이 있을 수 있다.

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";

    unordered_map<string, int> hash_map;
    
    for(const auto& a : completion) {
        hash_map[a]++;
    }

    for(const auto& b : participant) {
        hash_map[b]--;
        if(hash_map[b]==-1){
            answer = b;
        }
    }

    return answer;
}