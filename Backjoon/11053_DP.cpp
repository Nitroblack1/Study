#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    cin.ignore();

    string line;
    getline(cin, line);
    stringstream ss(line);
  
    int x;
    vector<int> nums;
    while(ss >> x) {
        nums.push_back(x);
    }

    vector<int> dp(n, 1);

    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }

    int ans = 0;
    for (int i = 0; i < n; i++) {
        ans = max(ans, dp[i]);
    }

    cout << ans;
    return 0;
}