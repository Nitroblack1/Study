#include <bits/stdc++.h>
using namespace std;

vector<vector<char>> board;

void draw(int n, int y, int x) {
    if (n == 1) {
        board[y][x] = '*';
        return;
    }

    int h = 4 * n - 1;
    int w = 4 * n - 3;
    int top = y;
    int bot = y + h - 1;
    int left = x;
    int right = x + w - 1;

    // 위, 아래 가로줄
    for (int i = left; i <= right; i++) {
        board[top][i] = '*';
        board[bot][i] = '*';
    }

    // 왼쪽 세로줄 (전부)
    for (int i = top; i <= bot; i++) board[i][left] = '*';
    // 오른쪽 세로줄 (윗쪽 2칸 비우고 아래부터)
    for (int i = top + 2; i <= bot; i++) board[i][right] = '*';

    // 내부 왼쪽 세로줄 (빈 공간 채워주기)
    for (int i = top + 2; i <= bot - 2; i++) board[i][left + 2] = '*';

    // 안쪽 프레임의 윗줄 연결
    for (int i = right - 2; i <= right; i++) board[top + 2][i] = '*';

    // 재귀
    draw(n - 1, y + 2, x + 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    if (n == 1) {
        cout << "*\n";
        return 0;
    }

    int h = 4 * n - 1;
    int w = 4 * n - 3;
    board.assign(h, vector<char>(w, ' '));

    draw(n, 0, 0);

    // 오른쪽 공백 제거 출력
    for (int i = 0; i < h; i++) {
        int end = w - 1;
        while (end >= 0 && board[i][end] == ' ') end--;
        for (int j = 0; j <= end; j++) cout << board[i][j];
        cout << '\n';
    }

    return 0;
}
