#include <iostream>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, w, L;
    cin >> n >> w >> L;

    queue<int> trucks;
    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        trucks.push(x);
    }

    queue<int> bridge; // 다리 위 상태
    int time = 0;
    int current_weight = 0;

    // 다리 초기 상태는 0으로 채워짐
    for (int i = 0; i < w; i++) bridge.push(0);

    while (!bridge.empty()) {
        time++;

        // 1. 다리 끝에서 트럭이 내려감
        current_weight -= bridge.front();
        bridge.pop();

        // 2. 새 트럭이 올라갈 수 있으면 올림
        if (!trucks.empty()) {
            if (current_weight + trucks.front() <= L) {
                bridge.push(trucks.front());
                current_weight += trucks.front();
                trucks.pop();
            } else {
                // 못 올라가면 빈 자리(0)로 채움
                bridge.push(0);
            }
        }
    }

    cout << time;
    return 0;
}