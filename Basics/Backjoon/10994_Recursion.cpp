#include <iostream>
#include <vector>
using namespace std;

void fill(vector<vector<char>> &board, int level, int start) {
    int len = 4 * (level - 1) + 1;
    int end = start + len - 1;

    // 테두리 채우기
    for (int i = start; i <= end; i++) {
        board[start][i] = '*';   // 위쪽
        board[end][i] = '*';     // 아래쪽
        board[i][start] = '*';   // 왼쪽
        board[i][end] = '*';     // 오른쪽
    }

    // 재귀 종료 조건
    if (level == 1) return;

    // 내부로 들어가기
    fill(board, level - 1, start + 2);
}

void draw_star(int n) {
    int size = 4 * (n - 1) + 1;
    vector<vector<char>> board(size, vector<char>(size, ' '));

    fill(board, n, 0);

    // 출력
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            cout << board[i][j];
        }
        cout << '\n';
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    draw_star(n);
    return 0;
}