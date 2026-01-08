/*순열조합(permutation combination)
순열은 순서가 부여된 임의의 집합을 다른 순서로 뒤섞는 연산이며
조합은 집합에서 일부 원소를 취해 부분 집합을 만드는 방법을 말한다.

주어진 문자열 str (길이 n)에 대해 아래 두 가지를 차례로 출력하시오.
1. str의 n개 character를 일렬로 배열하는 모든 경우를 출력하시오.
2. str의 n개 character 중 k개를 취하는 모든 경우를 출력하시오.

제한사항: 주어진 string에 동일한 알파벳이 중복으로 포함되지 않음.
String의 maximum size는 10. k <= n.
*/

#include <iostream>
#include <string>

using namespace std;

string combinationStack;

void swapChar(char &x, char &y) {
    char temp = x;
    x = y;
    y = temp;
}

void permutation(string &str, int l, int r) {
    if (l == r) {
        cout << str << '\n';
    } else {
        for (int i = l; i <= r; i++) {
            swapChar(str[l], str[i]);
            permutation(str, l + 1, r);
            swapChar(str[l], str[i]); // backtrack
        }
    }
}

void combination(string &str, int length, int offset, int k) {
    if (k == 0) {
        cout << combinationStack << '\n';
        return;
    }

    for (int i = offset; i <= length - k; i++) {
        combinationStack.push_back(str[i]);
        combination(str, length, i + 1, k - 1);
        combinationStack.pop_back(); // backtrack
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    for (int test_case = 1; test_case <= T; test_case++) {
        string str;
        int N, K;

        cin >> str >> N >> K;

        if ((int)str.size() > N) str.resize(N);

        cout << "#" << test_case << "\n";

        permutation(str, 0, N - 1);

        combinationStack.clear();
        combination(str, N, 0, K);
    }

    return 0;
}