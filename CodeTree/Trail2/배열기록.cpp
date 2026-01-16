#include <iostream>

using namespace std;

int N, M;
int v[1000], t[1000];
int v2[1000], t2[1000];
int A[1000000], B[1000000];

int main() {
    cin >> N >> M;
    int tA = 1, tB = 1;
    int tSum = 0;

    for (int i = 0; i < N; i++) {
        cin >> v[i] >> t[i];
        tSum += t[i];
    }

    for (int i = 0; i < M; i++) {
        cin >> v2[i] >> t2[i];
    }

    // A 기록
    for (int i = 0; i < N; i++) {
        while (t[i]--) {
            A[tA] = A[tA - 1] + v[i];
            tA++;
        }
    }

    // B 기록
    for (int i = 0; i < M; i++) {
        while (t2[i]--) {
            B[tB] = B[tB - 1] + v2[i];
            tB++;
        }
    }

    string leader = "AB";
    int cnt = 0;
    for (int i = 0; i < tSum; i++) {
        if (leader == "A") {
            if (A[i] == B[i]) {
                cnt++;
                leader = "AB";
            } else if (A[i] < B[i]) {
                cnt++;
                leader = "B";
            }
        } else if (leader == "B") {
            if (A[i] == B[i]) {
                cnt++;
                leader = "AB";
            } else if (A[i] > B[i]) {
                cnt++;
                leader = "A";
            }
        } else {
            if (A[i] > B[i]) {
                cnt ++;
                leader = "A";
            } else if (A[i] < B[i]) {
                cnt++;
                leader = "B";
            }
        }
    }

    cout << cnt;

    return 0;
}