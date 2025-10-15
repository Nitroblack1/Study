#include <iostream>
#include <queue>
#include <stack>
#include <vector>
using namespace std;

int pop_and_push(queue<pair<int, int>> *rail) {
    pair<int, int> temp = rail->front();
    rail->pop();
    rail->push(temp);
    return temp.second;
}

int reallocate(stack<pair<int, int>> *temp, stack<pair<int, int>> *space, pair<int, int> target) {
    int fee = 0;
    // 무게 규칙 위반한(더 가벼운) 것들을 전부 꺼낸다
    while (!space->empty() && space->top().second < target.second) {
        temp->push(space->top());
        fee += space->top().second; // 꺼낼 때
        space->pop();
    }

    // 새 컨테이너 적재
    space->push(target);
    fee += target.second;

    // 꺼낸 것들 다시 올리기
    while(!temp->empty()) {
        space->push(temp->top());
        fee += temp->top().second; // 다시 올릴 때
        temp->pop();
    }

    return fee;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    queue<pair<int, int>> rail;
    vector<stack<pair<int, int>>> spaces(m + 1); // 우선순위별 적재공간
    stack<pair<int, int>> temp;

    vector<int> total(m + 1, 0); // 각 우선순위별 총 개수
    vector<int> done(m + 1, 0);  // 적재 완료 개수

    for (int i = 0; i < n; i++) {
        int p, w;
        cin >> p >> w;
        rail.push({p, w});
        total[p]++;
    }

    long long fee = 0;

    // 우선순위 높은 것(숫자 큰 것)부터 전부 처리
    int turn = m;
    while (turn >= 1) {
        if (done[turn] == total[turn]) {
            // 현재 우선순위 컨테이너를 다 처리했으면 다음 우선순위로
            turn--;
            continue;
        }

        auto cur = rail.front();
        rail.pop();

        // 아직 더 낮은 우선순위(숫자가 큰 것)가 남아있으면 앞으로 보낸다
        bool lowerRemaining = false;
        for (int q = turn + 1; q <= m; q++) {
            if (done[q] < total[q]) {
                lowerRemaining = true;
                break;
            }
        }

        if (lowerRemaining) {
            fee += cur.second;
            rail.push(cur);
            continue;
        }

        // 지금 처리하려는 컨테이너의 우선순위가 현재 turn과 다르면 앞으로 보낸다
        if (cur.first != turn) {
            fee += cur.second;
            rail.push(cur);
            continue;
        }

        // 같은 우선순위라면 무게 조건에 따라 재배치 처리
        fee += reallocate(&temp, &spaces[turn], cur);
        done[turn]++;
    }

    cout << fee << "\n";
    return 0;
}
