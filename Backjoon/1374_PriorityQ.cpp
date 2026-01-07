#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<pair<int, int>> lec(N);

    for (int i = 0; i < N; i++) {
        int id, s, e;
        cin >> id >> s >> e;
        lec.push_back({s, e});
    }

    sort(lec.begin(), lec.end());   // 시작 시간 기준 오름차순 정렬

    priority_queue<int, vector<int>, greater<int>> pq; // 종료 시간 기준 최소 힙

    for (const auto& [s, e] : lec) {
        if (!pq.empty() && pq.top() <= s) {
            pq.pop();
        }
        pq.push(e);
    }

    cout << pq.size() << "\n";
    return 0;
}