#include <iostream>

using namespace std;

int main() {
    // 변수 선언 및 입력
    string binary;
    cin >> binary;
    
    // 십진수로 변환합니다.
    int num = 0;
    for(int i = 0; i < (int) binary.size(); i++)
        num = num * 2 + (binary[i] - '0');  // char to int, string의 i번째 원소(char 취급) 역시 이렇게 형변환 가능.
    
    // 출력
    cout << num;
    return 0;
}

/*
#include <iostream>

using namespace std;

int N, B;

int main() {
    cin >> N >> B;

    // Please write your code here.
    int arr[10], cnt = 0;
    while (N >= B) {
        arr[cnt++] = N % B;
        N /= B;
    }
    arr[cnt] = N;

    for (int i = cnt; i >= 0; i--) {
        cout << arr[i];
    }

    return 0;
}
*/

/*
#include <iostream>

using namespace std;

string N;

int main() {
    cin >> N;

    int num = 0;
    // Please write your code here.
    for (int i = 0; i < N.length(); i++) {
        num = num * 2 +  (N[i] - '0');
    }

    num *= 17;

    int a[10], cnt = 0;

    while(num >= 2) {
        a[cnt++] = num % 2;
        num /= 2;
    }
    a[cnt] = num;

    for (int i = cnt; i >= 0; i--) {
        cout << a[i];
    }

    return 0;
}
*/

/*
#include <iostream>

using namespace std;

int a, b;
string n;

int main() {
    cin >> a >> b;
    cin >> n;

    // Please write your code here.
    int num = 0;
    for (int i = 0; i < n.length(); i++) {
        num = num * a + (n[i] - '0');
    }

    int arr[10], cnt = 0;
    while (num >= b) {
        arr[cnt++] = num % b;
        num /= b;
    }
    arr[cnt] = num;

    for (int i = cnt; i >= 0; i--) {
        cout << arr[i];
    }

    return 0;
}
*/