#include <iostream>
#include <algorithm>    // for std::swap
using namespace std;

#define MAX_SIZE 100

int heap[MAX_SIZE];
int heapSize = 0;

void heapInit() {
    heapSize = 0;
}

bool heapPush(int value) {
    if (heapSize >= MAX_SIZE) {
        cout << "queue is full!" << endl;
        return false;
    }

    heap[heapSize] = value;
    int current = heapSize;

    while (current > 0 && heap[current] < heap[(current - 1) / 2]) {
        swap(heap[current], heap[(current - 1) / 2]);
        current = (current - 1) / 2;
    }

    heapSize++;
    return true;
}

bool heapPop(int &value) {
    if (heapSize <= 0) {
        return false;
    }

    value = heap[0];
    heapSize--;
    heap[0] = heap[heapSize];

    int current = 0;

    while (current * 2 + 1 < heapSize) {
        int left = current * 2 + 1;
        int right = current * 2 + 2;
        int child = left;

        if (right < heapSize && heap[right] < heap[left]) {
            child = right;
        }

        if (heap[current] <= heap[child]) break;

        swap(heap[current], heap[child]);
        current = child;
    }

    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T, N;
    cin >> T;

    for (int test_case = 1; test_case <= T; test_case++) {
        cin >> N;

        heapInit();

        for (int i = 0; i < N; i++) {
            int value;
            cin >> value;
            heapPush(value);
        }

        cout << "#" << test_case << " ";

        for (int i = 0; i < N; i++) {
            int value;
            heapPop(value);
            cout << value << " ";
        }

        cout << "\n";
    }

    return 0;
}