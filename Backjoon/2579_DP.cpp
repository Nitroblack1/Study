#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int score[n];
    int dp[n];

    for (int i = 0; i < n; i++) {
        cin >> score[i];
    }

    if (n == 1) {
        cout << score[0];
        return 0;
    }

    if (n == 2) {
        cout << score[0] + score[1];
        return 0;
    }

    // dp initialization
    for (int i = 0; i < n; i++) {
        dp[i] = -1;
    }

    
    dp[0] = score[0];
    dp[1] = score[0] + score[1];
    dp[2] = max(score[0] + score[2], score[1] + score[2]);

    for (int i = 3; i < n; i++) {
        dp[i] = max(dp[i - 2] + score[i], dp[i - 3] + score[i - 1] + score[i]);
    }

    cout << dp[n-1];
}