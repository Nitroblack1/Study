#include <string>
#include <iostream>
#include <stack>
using namespace std;

int main() {
    string line;
    cin >> line;
    int ans = 0;

    stack<char> stk;

    int i = 0;
    while (i < line.length()) {
        if (line[i] == '(') {
            stk.push('(');
        } else if (line[i - 1] == ')') {
            stk.pop();
            ans += 1;
        } else {
            stk.pop();
            ans += stk.size();
        }
        i++;
    }

    cout << ans;
}