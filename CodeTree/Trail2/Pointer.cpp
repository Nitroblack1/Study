#include <iostream>

using namespace std;

/*
C/C++ Ver.

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
    cout << *a << " " << *b << endl;
}

int main() {
    int n = 10, m = 20;
    swap(&n, &m);
    cout << n << " " << m;
    return 0;
}
*/


void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

void Modify(int *x) {   // 배열 수정
    cout << x[0] << endl;
    cout << x[1] << endl;

    x[0] = 100;
}

void Modify2(int x[]) {
    cout << x[0] << endl;
    cout << x[1] << endl;

    x[0] = 100;
}

void Modify(int &a, int &b) {
    if (a >= b) {
        a += 25;
        b *= 2;
    } else {
        a *= 2;
        b += 25;
    }
}

int main() {
    int n, m;
    cin >> n >> m;

    // Please write your code here.
    swap(n, m);
    cout << n << " " << m;

    int arr[4] = {5, 6, 9, 2};

    cout << *arr << endl;           // 5
    cout << *(arr + 1) << endl;     // 6
    cout << *(arr + 2) << endl;     // 9


    return 0;
}