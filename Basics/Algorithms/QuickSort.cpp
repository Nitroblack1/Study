#include <iostream>
using namespace std;

#define MAX_NUM 100

int input[MAX_NUM];
int num;

void quickSort(int first, int last) {
    int pivot;
    int i;
    int j;
    int temp;

    if (first < last) {
        pivot = first;  // 첫 번째 원소를 피봇으로
        i = first;
        j = last;

        while (i < j) {
            while (input[i] <= input[pivot] && i < last) {
                i++;
            }

            while (input[j] > input[pivot]) {
                j--;
            }

            if (i < j) {
                temp = input[i];
                input[i] = input[j];
                input[j] = temp;
            }
        }

        temp = input[pivot];
        input[pivot] = input[j];
        input[j] = temp;

        quickSort(first, j - 1);
        quickSort(j + 1, last);
    }
}

void printResult() {
    int i;
    for (i = 0; i < num; ++i) {
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
        for (int i = 0; i < num; i++) {
            cin >> input[i];
        }
        quickSort(0, num - 1);
        cout << "#" << test_case << ' ';
        printResult();
    }

    return 0;
}