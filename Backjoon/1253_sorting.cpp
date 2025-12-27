#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<long long> numbers(N);
    for (int i = 0; i < N; i++) {
        cin >> numbers[i];
    }

    sort(numbers.begin(), numbers.end());

    int good = 0;

    for (int i = 0; i < N; i++) {
        int l = 0, r = N - 1;
        while (l < r) {
            if (l == i) {
                l++;
                continue;
            }
            if (r == i) {
                r--;
                continue;
            }

            long long sum = numbers[l] + numbers[r];
            if (sum == numbers[i]) {
                good++;
                break;
            } else if (sum < numbers[i]) {
                l++;
            } else {
                r--;
            }
        }
    }

    cout << good << "\n";
    return 0;
}