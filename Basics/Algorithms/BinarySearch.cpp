#include <iostream>

using namespace std;

#define MAX_N 100

int T, M, N, arr[MAX_N];

void binarySearch(int* arr, int low, int high, int target) {
    if (low > high) {
        cout << "-1 ";
        return;
    }

    int mid = (low + high) / 2;

    if (target < arr[mid]) {
        binarySearch(arr, low, mid - 1, target);
    } else if (arr[mid] < target) {
        binarySearch(arr, mid + 1, high, target);
    } else {
        cout << mid << " ";
        return;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> T;

    for (int test_case = 1; test_case <= T; test_case++) {
        cout << "#" << test_case << " ";

        cin >> M >> N;

        for (int i = 0; i < M; i++) {
            cin >> arr[i];
        }

        for (int i = 0; i < N; i++) {
            int targetValue;
            cin >> targetValue;
            binarySearch(arr, 0, M - 1, targetValue);
        }

        cout << "\n";
    }

    return 0;
}