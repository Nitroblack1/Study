#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<string> grid(N);
    for (int i = 0; i < N; i++) cin >> grid[i];

    vector<vector<int>> dist(N, vector<int>(M, 0));
    queue<pair<int,int>> q;

    // 시작점 (0,0)
    dist[0][0] = 1;
    q.push({0, 0});

    int dr[4] = {-1, 1, 0, 0};
    int dc[4] = {0, 0, -1, 1};

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        for (int k = 0; k < 4; k++) {
            int nr = r + dr[k];
            int nc = c + dc[k];

            if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue; // 범위 밖
            if (grid[nr][nc] == '0') continue;                    // 벽
            if (dist[nr][nc] != 0) continue;                      // 이미 방문

            dist[nr][nc] = dist[r][c] + 1;
            q.push({nr, nc});
        }
    }

    cout << dist[N-1][M-1] << "\n";
    return 0;
}
