#include <iostream>
#include <sstream>
#include <stack>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    cin.ignore();
    
    vector<int> height(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> height[i];
    }

    stack<pair<int, int>> st;
    vector<int> result(n + 1, 0);

    for (int i = 1; i <= n; i++) {
        while (!st.empty() && st.top().first < height[i]) {
            st.pop();
        }

        if (!st.empty()) {
            result[i] = st.top().second;
        } else {
            result[i] = 0;
        }

        st.push({height[i], i});
    }

    for (int i = 1; i <= n; i++) {
        cout << result[i] << " ";
    }

    cout << '\n';
}