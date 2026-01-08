#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    int min;

    vector<int> times(N);

    for (int i = 0; i < N; i++) {
        cin >> times[i];
    }

    long long minT = *min_element(times.begin(), times.end());

    long long low = 1;
    long long high = minT * M;
    long long answer = high;

    while (low <= high) {
        long long mid = (low + high) / 2;
        long long total = 0;

        for (int i = 0; i < N; i++) {
            total += mid / times[i];
            if (total >= M) {
                break;
            }
        }

        if (total >= M) {
            answer = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << answer << endl;
    return 0;
}