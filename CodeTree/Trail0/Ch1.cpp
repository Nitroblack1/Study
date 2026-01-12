#include <iostream>
#include <string>
using namespace std;

#define MAX_N 100

void decimal_point() {
    int a = 13;
    double rate = 0.165;

    cout << fixed;
    cout.precision(6);

    cout << a << " * " << rate << " = " << a * rate;
}

void str_stoi_stod() {
    string text = "CodeTree";
    string g = "20";
    string h = "14.5";

    cout << text[0] << text[4] << endl;
    text[4] = 't';
    cout << text << endl;
    cout << stoi(g) + 5 << endl;
    cout << stod(h) + 3.3 << endl;
}

void string_methods() {
    string text = "CodeTree";
    string subt1 = "Code";
    string subt2 = "Tree";

    cout << text.size() << endl;
    cout << text.substr(4) << endl;
    cout << text.substr(4, 4);      // index 4부터 길이 4만큼 출력하라.
    cout << subt1 + subt2;
}

void varInLoop() {
    string words[5] = {"apple", "banana", "grape", "blueberry", "orange"};
    char spell;
    cin >> spell;

    int answer = 0;

    for (const auto& word : words) {
        if (word[2] == spell || word[3] == spell) {
            answer += 1;
            cout << word << endl;
        }
    }

    cout << answer;
}

void specialCharbetweenNum() {
    int a, b, c;
    char d;

    cin >> a >> d >> b >> d >> c;
    
    cin >> a;
    cin.get();
    cin >> b;
    cin.get();
    cin >> c;
}

int main() {
    decimal_point();
    return 0;
}
