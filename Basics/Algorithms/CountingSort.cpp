#include <iostream>
using namespace std;

#define MAX_N 100
#define MAX_DIGIT 10

int N;
int arr[MAX_N];
int cnt[MAX_DIGIT];
int sortedArr[MAX_N];

void calculateDigitNumber() {
    for (int i = 0; i < N; i++) {
        cnt[arr[i]]++;
    }

    for (int i = 1; i < MAX_DIGIT; i++) {
        cnt[i] += cnt[i - 1];
    }
}

void executeCountingSort() {
    for (int i = N - 1; i >= 0; i--) {
        sortedArr[--cnt[arr[i]]] = arr[i];
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    for (int test_case = 1; test_case <= T; test_case++) {
        cin >> N;

        for (int i = 0; i < N; i++) {
            cin >> arr[i];
        }

        // initialize count array
        for (int i = 0; i < MAX_DIGIT; i++) {
            cnt[i] = 0;
        }

        calculateDigitNumber();
        executeCountingSort();

        cout << "#" << test_case << " ";
        for (int i = 0; i < N; i++) {
            cout << sortedArr[i] << " ";
        }
        cout << "\n";
    }

    return 0;
}