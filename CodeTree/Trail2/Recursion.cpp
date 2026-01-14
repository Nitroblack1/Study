#include <iostream>
#include <algorithm>

using namespace std;

int N;

void PrintStar(int n) {
    /*
    output ex)
    ****
    ***
    **
    *
    *
    **
    ***
    ****
    */
    if(n == 0)
        return;

    for(int i = 0; i < n; i++)
        cout << "*";
    cout << endl;
    PrintStar(n - 1);
    for(int i = 0; i < n; i++)
        cout << "*";
    cout << endl;
}

int DivideEx(int n) {
    if (n == 1) {
        return 0;
    }

    if (n % 2 == 0) {
        return DivideEx(n / 2) + 1;
    } else {
        return DivideEx(n / 3) + 1;
    }
}

// a번째 까지 인덱스의 숫자 중에 가장 큰 값을 반환합니다.
int MaxValue(int *arr, int a) {
    if(a == 0)
        return arr[0];

    return max(MaxValue(arr, a - 1), arr[a]);
}


int cur = 1;
int arr[100];
int n;
int GCD(int a, int b) {
    int cd = 1;
    int min = (a >= b) ? b : a;

    for (int i = 2; i <= min; i++) {
        if (a % i == 0 && b % i == 0) {
            cd = i;
        }
    }
    return cd;
}

int f(int N) {
    if (N == n) return cur;
    cur = (arr[N]*cur) / GCD(arr[N], cur);
    return f(N + 1);
}


int main() {
    cin >> N;

    return 0;
}