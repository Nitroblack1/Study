#include <iostream>
#include <string>
#include <math.h>
using namespace std;

bool isPelindrom(string testString) {
    for (int i = 0; i < floor(testString.length() / 2); i++) {
        if (testString[i] != testString[testString.length() - i - 1]) {
            return false;
        }
    }
    return true;
}

bool checkPel(string strs) {
    // if baseCamp, return true
    if (strs.length() == 1) {
        return true;
    }

    int len = floor(strs.length() / 2);
    string front = strs.substr(0, len);
    string back = strs.substr(strs.length() - len, len);
    // floor(|S|/2) recursion fn call
    if (!checkPel(front) or !checkPel(back)) {
        return false;
    }

    // check 1st condition
    if (!isPelindrom(strs)) {
        return false;
    }

    // check 2nd condition
    if (!isPelindrom(front) or !isPelindrom(back)) {
        return false;
    }

    return true;
}

int main() {
    string S;
    cin >> S;

    cout << ((checkPel(S)) ? "AKARAKA" : "IPSELENTI");

    return 0;
}