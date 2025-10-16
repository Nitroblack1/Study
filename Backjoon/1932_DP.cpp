#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    cin.ignore();

    vector<vector<int>> map(n); 
    vector<vector<int>> dp(n);

    for (int i = 0; i < n; i++) {
        string line;
        getline(cin, line);
        stringstream ss(line);
        int x;
        while (ss >> x) {
            map[i].push_back(x);
            dp[i].push_back(0);
        }
    }

    dp[0][0] = map[0][0];
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < map[i].size(); j++) {
            // 만약 왼쪽 가장자리 라인이면
            if (j == 0) {
                dp[i][j] = dp[i-1][j] + map[i][j];
            // 오른쪽 가장자리 라인이면
            } else if (j == map[i].size() - 1) {
                dp[i][j] = dp[i-1][j-1] + map[i][j];
            // 그 외 라인이면
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + map[i][j];
            }
        }
    }

    // 현재 index 기준 동일 or +1만 가능
    // dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + dp[i][j]

    int ans = 0;
    for (int k = 0; k < n; k++) {
        ans = max(ans, dp[n-1][k]);
    }
    cout << ans;
}