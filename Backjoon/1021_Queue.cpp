#include <iostream>
#include <deque>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    deque<int> dq;
    for (int i = 1; i <= N; i++) dq.push_back(i);

    int ans = 0;

    for (int i = 0; i < M; i++) {
        int target;
        cin >> target;

        int idx = 0;
        for (int j = 0; j < dq.size(); j++) {
            if (dq[j] == target) {
                idx = j;
                break;
            }
        }

        // 왼쪽 회전이 빠른 경우
        if (idx <= dq.size() / 2) {
            while (dq.front() != target) {
                dq.push_back(dq.front());
                dq.pop_front();
                ans++;
            }
        }
        // 오른쪽 회전이 빠른 경우
        else {
            while (dq.front() != target) {
                dq.push_front(dq.back());
                dq.pop_back();
                ans++;
            }
        }

        dq.pop_front(); // 첫 번째 원소 제거
    }

    cout << ans << '\n';
    return 0;
}
