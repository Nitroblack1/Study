#include <iostream>
using namespace std;

void diamond() {
    int n;
    cin >> n;

    for (int row = n; row > 0; row--) {
        for (int i = 1; i < row; i++) {
            cout << " ";
        }
        for (int j = 0; j <= n - row; j++) {
            cout << "*" << " ";
        }
        cout << endl;
    }

    for (int row = 1; row < n; row++) {
        for (int i = 0; i < row; i++) {
            cout << " ";
        }
        for (int j = 0; j < n - row; j++) {
            cout << "*" << " ";
        }
        cout << endl;
    }
}

void innerDiamond() {
    int n;
    cin >> n;

    for (int row = n; row > 0; row--) {
        for (int star = row; star > 0; star--) {
            cout << "*";
        }

        for (int space = n - row; space > 0; space--) {
            cout << " ";
        }

        for (int space = n - row; space > 0; space--) {
            cout << " ";
        }

        for (int star = row; star > 0; star--) {
            cout << "*";
        }
        cout << endl;
    }
}

void rowReliedPrint() {
    int n;
    cin >> n;

    for(int i = 1; i <= 2 * n; i++) {
        if (i % 2 == 1) {
            for(int odd = 0; odd <= 2 * n - i; odd += 2) {
                cout << "*" << " ";
            }
            cout << endl;
        } else {
            for(int even = 0; even < i / 2; even++) {
                cout << "*" << " ";
            }
            cout << endl;
        }
    }
}

void randomPattern1() {
    int n;
    cin >> n;

    for(int i = 0; i < n; i++) {
        if (i == 0 || i == n-1) {
            for(int j = 0; j < n; j++) {
                cout << "* ";
            }
            cout << endl;
        } else {        // i <= j 식의 조건도 적극 고려해보자.
            cout << "* ";
            for (int j = 0; j < i - 1; j++) {
                cout << "* ";
            }
            for (int k = 0; k < n - i - 1; k++) {
                cout << "  ";
            }
            cout << "*" << endl;
        }
    }
}

void numPattern1() {
    /*
    input : 5
    output : 
    5 4 3 2 1
    10 8 6 4 2
    15 12 9 6 3
    20 16 12 8 4
    25 20 15 10 5
    */
    int n;
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cout << i * (n - j + 1) << " ";
        }
        cout << endl;
    }
}

void usingCntPattern1() {
    /*
    input : 4
    output :
    9876
    5432
    1987
    6543
    */
    int n, cnt = 9;
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (cnt == 1) {
                cout << cnt;
                cnt = 9;
            }
            else {
                cout << cnt--;
            }
        }
        cout << endl;
    }
}

void usingCntPattern2() {
    /*
    input : 4
    output :
    1 2 3 4
    6 8 10 12
    13 14 15 16
    18 20 22 24
    */
    int n, cnt = 1;
    cin >> n;

    for (int row = 1; row <= n; row++) {
        if (row % 2 == 1) {
            for (int rep = 0; rep < n; rep++) {
                cout << cnt++ << " ";
            }
            cout << endl;
            cnt += 1;
        } else {
            for (int rep = 0; rep < n; rep++) {
                cout << cnt << " ";
                cnt += 2;
            }
            cout << endl;
            cnt -= 1;
        }
    }
}

void mulTable() {
    int a, b;
    cin >> a >> b;

    for (int num = 2; num <= 8; num += 2) {
        for (int col = b; col > a; col--) {
            cout << col << " * " << num << " = " << col*num << " / ";
        }
        cout << a << " * " << num << " = " << a*num << endl;
    }
}

void numPattern2() {
    /*
    input : 5
    output : 
    5
    4 5
    3 4 5
    2 3 4 5
    1 2 3 4 5
    */
   int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = i; j >= 0; j--) {
            cout << n - j << " ";
        }
        cout << endl;
    }
}

int main() {
    
}