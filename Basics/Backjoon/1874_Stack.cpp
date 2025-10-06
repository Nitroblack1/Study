#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> target(n);
    for (int i = 0; i < n; i++) cin >> target[i];

    stack<int> st;
    vector<char> ops;
    int cur = 1;

    for (int x : target) {
        while (cur <= x) {
            st.push(cur++);
            ops.push_back('+');
        }

        if (!st.empty() && st.top() == x) {
            st.pop();
            ops.push_back('-');
        } else {
            cout << "NO";
            return 0;
        }
    }

    for (char op : ops) {
        cout << op << '\n';
    }
}