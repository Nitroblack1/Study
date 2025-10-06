#include <iostream>

int main() {
    int n;
    std::cin >> n;

    int dp[n + 1];

    if (n == 1) {
        std::cout << 1;
        return 0;
    }

    if (n == 2) {
        std::cout << 2;
        return 0;
    }

    for (int i = 0; i < n; i++) {
        dp[i] = -1;
    }

    dp[1] = 1;
    dp[2] = 2;
    
    for (int i = 3; i <= n; i++) {
        dp[i] = (dp[i-1] + dp[i-2]) % 10007;
    }

    std::cout << (dp[n]);
}