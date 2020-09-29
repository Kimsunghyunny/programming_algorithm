#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

//수록 순서 1.많이 재생된 장르 2.장르내 많이 재생된 3.재생수가 같으면 고유번호 오름차순
//장르에 따른 해시 테이블을 만든다.
//해시 테이블을 <string, vector<pair<<int, int>>>로 해서 장르에 따른 고유번호와 재생횟수를 같이 저장해주도록 한다.

bool compare(pair<int, int> a, pair<int, int> b);
bool compare_count(pair<string, int> a, pair<string, int> b);

vector<int> solution(vector<string> genres, vector<int> plays)
{
    vector<int> answer;

    unordered_map<string, vector<pair<int, int>>> playlist;
    unordered_map<string, int> genre_count;

    for (int i = 0; i < genres.size(); i++)
    {
        playlist[genres[i]].push_back(make_pair(i, plays[i])); //장르에 따른 고유번호와 재생횟수 저장하는 해시테이블
        genre_count[genres[i]] += plays[i];                    // 장르 재생횟수 저장하는 해시테이블
    }

    //수록 순서에 따라 answer에 들어가도록 한다. sort로 해시 테이블 정렬한다.
    for (auto &a : playlist)
    { //장르에 따른 고유번호,재생횟수 해시테이블 정렬
        sort(a.second.begin(), a.second.end(), compare);
    }

    vector<pair<string, int>> genre_count_v;
    genre_count_v.assign(genre_count.begin(), genre_count.end());
    sort(genre_count_v.begin(), genre_count_v.end(), compare_count);

    for (int i = 0; i < genre_count_v.size(); i++) //장르가 같은 것을 playlist에서 찾아서 answer에 차례로 넣어주기.
    {
        string name = genre_count_v[i].first;
        for (int j = 0; j < playlist[name].size() && j < 2; j++)
        { //해당 장르
            answer.push_back(playlist[name][j].first);
        }
    }

    return answer;
}

bool compare(pair<int, int> a, pair<int, int> b)
{
    if (a.second == b.second)
    {
        return a.first < b.first;
    }
    else
    {
        return a.second > b.second;
    }
}

bool compare_count(pair<string, int> a, pair<string, int> b)
{
    return a.second > b.second;
}
