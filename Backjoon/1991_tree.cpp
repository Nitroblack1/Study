#include <iostream>
#include <vector>
#include <functional>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<char> leftC(26, '.'), rightC(26, '.');

    for (int i = 0; i < N; i++) {
        char p, l, r;
        cin >> p >> l >> r;
        int idx = p - 'A';
        leftC[idx] = l;
        rightC[idx] = r;
    }

    function<void(char)> preorder = [&](char cur) {
        if (cur == '.') return;
        cout << cur;
        preorder(leftC[cur - 'A']);
        preorder(rightC[cur - 'A']);
    };

    function<void(char)> inorder = [&](char cur) {
        if (cur == '.') return;
        inorder(leftC[cur - 'A']);
        cout << cur;
        inorder(rightC[cur - 'A']);
    };

    function<void(char)> postorder = [&](char cur) {
        if (cur == '.') return;
        postorder(leftC[cur - 'A']);
        postorder(rightC[cur - 'A']);
        cout << cur;
    };

    preorder('A');
    cout << '\n';
    inorder('A');
    cout << '\n';
    postorder('A');
    cout << '\n';

    return 0;
}
