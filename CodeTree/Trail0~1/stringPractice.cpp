#include <iostream>
#include <string>
#include <cctype>
using namespace std;

void getLinePractice() {
    string str1, str2;

    getline(cin, str1);
    getline(cin, str2);

    for (int i = 0; i < str1.length(); i++) {
        if (str1[i] == ' ') continue;
        cout << str1[i];
    }

    for (int i = 0; i < str2.length(); i++) {
        if (str2[i] == ' ') continue;
        cout << str2[i];
    }
}

void substr_eraseExample() {
    string s = "baknana";
    s = s.substr(0, 2) + s.substr(3);   // 0~1 index + 3~fin index
    cout << s;  // banana

    s = "baknana";
    s.erase(2, 1);  // 시작 인덱스와 그 인덱스로부터의 문자 개수
    cout << s;  // banana

    string str;
    cin >> str;

    str.erase(str.find("e"),1);
    cout << str;
}

void asciiExample() {
    char x;
    cin >> x;

    char ans = (x - 1 < 97) ? 122 : x-1;

    cout << ans;
}

void cctypeLibraryExample() {
    // #include <cctype> : tolower(), toupper(), isupper(), islower(), isalpha(), isdigit()
    string a;
    cin >> a;

    for (int i = 0; i < a.length(); i++) {
        if (islower(a[i])) a[i] = toupper(a[i]);
        else a[i] = tolower(a[i]);
    }

    cout << a;

    ////////////////////////////////////////////////
    // input :
    // 20code21
    // tr20ee22
    //
    // output : 4043
    string a, b;
    cin >> a >> b;

    string temp1 = {}, temp2 = {};

    for (int i = 0; i < a.length(); i++) {
        if (isdigit(a[i])) {
            temp1 += a[i];
        }
    }

    for (int i = 0; i < b.length(); i++) {
        if (isdigit(b[i])) {
            temp2 += b[i];
        }
    }

    cout << stoi(temp1) + stoi(temp2);

    ////////////////////////////////////////////////////////////////
    /*
    input : 5
            1234
            438
            23
            34
            348
    output : 0772
    */
    int n, sum = 0;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        sum += temp;
    }

    cout << to_string(sum).substr(1) + to_string(sum)[0];
}

int main() {
    return 0;
}