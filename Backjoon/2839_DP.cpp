#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> dp(n + 1);

    if (n == 3 || n == 5) {
        cout << "1";
        return 0;
    }

    if (n == 4) {
        cout << "-1";
        return 0;
    }

    for (int i = 0; i <= n; i++) {
        dp[i] = -1;
    }

    dp[3] = 1;
    dp[5] = 1;
    int rest = n;

    for (int i = 6; i <= n; i++) {
        if (dp[i - 3] != -1 && dp[i - 5] != -1) {
            dp[i] = min(dp[i - 3] + 1, dp[i - 5] + 1);
            continue;
        } else {
            if (dp[i - 3] != -1) {
                dp[i] = dp[i - 3] + 1;
                continue;
            }
            if (dp[i - 5] != -1) {
                dp[i] = dp[i - 5] + 1;
                continue;
            }
        }
    }

    if (dp[n] != -1 && dp[n] > 0) {
        cout << dp[n];
    } else {
        cout << "-1";
    }
}