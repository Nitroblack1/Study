#include <iostream>
using namespace std;

#define MAX_NUM 100

int input[MAX_NUM];
int num;

void insertionSort() {
    int temp;
    int i;
    int j;

    for (i = 1; i < num; i++) {
        temp = input[i];
        j = i-1;

        while ((j >= 0) && (temp < input[j])) {
            input[j + 1] = input[j];
            j--;
        }

        input[j + 1] = temp;
    }
}

void printResult() {
    int i;

    for(i = 0; i < num; ++i) {
        cout << input[i] << ' ';
    }
    cout << '\n';
}

int main() {
    int T;
    int test_case;
    int i;

    cin >> T;

    for (test_case = 1; test_case <= T; test_case++) {
        cin >> num;
        for (i = 0; i < num; i++) {
            cin >> input[i];
        }

        insertionSort();
        cout << "#" << ' ' << test_case << ' ';
        printResult();
    }
    return 0;
}