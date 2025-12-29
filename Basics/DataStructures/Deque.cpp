#include <iostream>
#include <vector>

using namespace std;

class Deque {
private:
    vector<int> arr;
    int frontIdx;
    int rearIdx;
    int sz; // capacity

public:
    explicit Deque(int n = 0) { init(n); }

    void init(int n) {
        sz = n;
        arr.assign(sz, 0);
        frontIdx = -1;
        rearIdx = 0;
    }

    bool isFull() const {
        return ((frontIdx == 0 && rearIdx == sz - 1) || (frontIdx == rearIdx + 1));
    }

    bool isEmpty() const {
        return (frontIdx == -1);
    }

    void insertFront(int value) {
        if (isFull()) {
            // C 코드처럼 메시지만 출력하고 계속 진행
            cout << "Overflow\n";
            return;
        }

        if (frontIdx == -1) {
            frontIdx = rearIdx = 0;
        } else if (frontIdx == 0) {
            frontIdx = sz - 1;
        } else {
            frontIdx -= 1;
        }

        arr[frontIdx] = value;
    }

    void insertRear(int value) {
        if (isFull()) {
            cout << "Overflow\n";
            return;
        }

        if (frontIdx == -1) {
            frontIdx = rearIdx = 0;
        } else if (rearIdx == sz - 1) {
            rearIdx = 0;
        } else {
            rearIdx += 1;
        }

        arr[rearIdx] = value;
    }

    int getFront() const {
        if (isEmpty()) {
            cout << "Underflow\n";
            return -1;
        }
        return arr[frontIdx];
    }

    int getRear() const {
        if (isEmpty() || rearIdx < 0) {
            cout << "Underflow\n";
            return -1;
        }
        return arr[rearIdx];
    }

    void deleteFront() {
        if (isEmpty()) {
            cout << "Underflow\n";
            return;
        }

        if (frontIdx == rearIdx) {
            frontIdx = -1;
            rearIdx = -1;
        } else if (frontIdx == sz - 1) {
            frontIdx = 0;
        } else {
            frontIdx += 1;
        }
    }

    void deleteRear() {
        if (isEmpty()) {
            cout << "Underflow\n";
            return;
        }

        if (frontIdx == rearIdx) {
            frontIdx = -1;
            rearIdx = -1;
        } else if (rearIdx == 0) {
            rearIdx = sz - 1;
        } else {
            rearIdx -= 1;
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T, N, M;
    cin >> T;

    for (int test_case = 1; test_case <= T; ++test_case) {
        cin >> N >> M;

        Deque dq(N);

        cout << "#" << test_case << " ";

        for (int i = 0; i < M; ++i) {
            int cmd;
            cin >> cmd;

            switch (cmd) {
                case 1: {
                    int elem;
                    cin >> elem;
                    dq.insertFront(elem);
                    break;
                }
                case 2: {
                    int elem;
                    cin >> elem;
                    dq.insertRear(elem);
                    break;
                }
                case 3:
                    cout << dq.getFront() << " ";
                    break;
                case 4:
                    cout << dq.getRear() << " ";
                    break;
                case 5:
                    dq.deleteFront();
                    break;
                case 6:
                    dq.deleteRear();
                    break;
            }
        }

        cout << "\n";
    }

    return 0;
}
