#include <iostream>
#include <string>

using namespace std;

int main() {

    string tmp;

    getline(cin, tmp);

    int index = tmp.find(" ");

    int a = stoi(tmp.substr(0,index));
    int b = stoi(tmp.substr(index+1));

    if (a < b)
        cout << "<" <<endl;
    else if (a > b)
        cout << ">" <<endl;
    else
        cout << "==" <<endl;

    
    return 0;

}