#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<pair<int, int>> events;
    events.reserve(2 * N);

    int id, s, e;
    for (int i = 0; i < N; i++) {
        cin >> id >> s >> e;

        events.push_back({s, 1});
        events.push_back({e, -1});
    }

    sort(events.begin(), events.end(), [](const auto& a, const auto& b) {
        if (a.first != b.first) return a.first < b.first;
        return a.second < b.second;
    });

    int cur = 0, ans = 0;
    for (const auto& ev : events) {
        cur += ev.second;
        if (cur > ans) {
            ans = cur;
        }
    }

    cout << ans << "\n";
    return 0;
}