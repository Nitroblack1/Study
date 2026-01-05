#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Node {
    int z, x, y;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int M, N, H;
    cin >> M >> N >> H;

    // box[z][x][y] : z = 층(0..H-1), x = 행(0..N-1), y = 열(0..M-1)
    vector<vector<vector<int>>> box(H, vector<vector<int>>(N, vector<int>(M)));

    queue<Node> q;

    for (int z = 0; z < H; z++) {
        for (int x = 0; x < N; x++) {
            for (int y = 0; y < M; y++) {
                cin >> box[z][x][y];
                if (box[z][x][y] == 1) {
                    q.push({z, x, y});
                }
            }
        }
    }

    // 6방향 (상하좌우 + 위아래)
    int dz[6] = {0, 0, 0, 0, 1, -1};
    int dx[6] = {1, -1, 0, 0, 0, 0};
    int dy[6] = {0, 0, 1, -1, 0, 0};

    // BFS
    while (!q.empty()) {
        Node cur = q.front();
        q.pop();

        for (int dir = 0; dir < 6; dir++) {
            int nz = cur.z + dz[dir];
            int nx = cur.x + dx[dir];
            int ny = cur.y + dy[dir];

            if (nz < 0 || nz >= H || nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
            if (box[nz][nx][ny] != 0) continue; // 0(안익음)

            box[nz][nx][ny] = box[cur.z][cur.x][cur.y] + 1; // 날짜 기록
            q.push({nz, nx, ny});
        }
    }

    // 결과 계산: 0 남아있으면 -1, 아니면 최댓값-1
    int mx = 1;
    for (int z = 0; z < H; z++) {
        for (int x = 0; x < N; x++) {
            for (int y = 0; y < M; y++) {
                if (box[z][x][y] == 0) { // 안 익은 토마토 존재
                    cout << -1 << "\n";
                    return 0;
                }
                mx = max(mx, box[z][x][y]);
            }
        }
    }

    cout << (mx - 1) << "\n";
    return 0;
}