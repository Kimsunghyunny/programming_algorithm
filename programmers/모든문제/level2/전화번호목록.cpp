//해시

#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

//어떤 번호가 다른 번호의 접두어인 경우가 있으면 false, 없으면 true를 return하도록 해라.
//substr(a,b) a=시작할 위치, b=자르려는 크기


/* 효율성 탈락
bool solution(vector<string> phone_book) {

    sort(phone_book.begin(), phone_book.end());
    unordered_map<string, int> h;
    
    for(int i=0; i<phone_book.size(); i++) {
        for(int j = i+1 ; j<phone_book.size(); j++) {
            if(phone_book[j].substr(0,phone_book[i].size()) == phone_book[i]) {
                h[phone_book[i]]++;
            }
        }
    }

    if (h.size() > 0) 
        return false;
    else 
        return true;
}

*/



bool solution(vector<string> phone_book) {
    bool answer = true;

    sort(phone_book.begin(), phone_book.end());
    unordered_map<string, int> h;

    for(auto a : phone_book) {
        string str;
        for(int i=0; i<a.size(); i++) {
            str += a[i];
            h[str]++;
        }
    }

    for(auto b : phone_book) {
           if(h[b] >1) {
               answer = false;
               break;
           }
    }

    return answer;
}
