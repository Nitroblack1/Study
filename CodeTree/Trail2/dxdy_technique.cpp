#include <iostream>

using namespace std;

string dirs;

// 북 동 남 서
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

int curDir;
pair<int, int> pos;

int main() {
    cin >> dirs;

    for (int i = 0; i < dirs.length(); i++) {
        if (dirs[i] == 'F') {
            pos.first += dx[curDir];
            pos.second += dy[curDir];
        } else if (dirs[i] == 'L') {
            curDir = (curDir + 3) % 4;
        } else if (dirs[i] == 'R') {
            curDir = (curDir + 1) % 4;
        }
    }

    cout << pos.first << " " << pos.second;

    return 0;
}

/*
#include <iostream>

using namespace std;

int n;
int grid[100][100];
int total;

// 우, 하, 좌, 상
int di[4] = {1, 0, -1, 0};
int dj[4] = {0, 1, 0, -1};

bool Inbound(int i, int j) {
    return (0 <= i && i < n) && (0 <= j && j < n);
}

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }

    int count, ni, nj;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            count = 0;
            for (int k = 0; k <= 3; k++) {
                ni = i + di[k];
                nj = j + dj[k];

                if (Inbound(ni, nj) && grid[ni][nj] == 1) {
                    count++;
                }
            }

            if (count >= 3) total++;
        }
    }

    cout << total;

    return 0;
}
*/

/*
#include <iostream>
#include <string>

#define ASCII_NUM 128
#define DIR_NUM 4

using namespace std;

int n, t;
int x, y, dir;
int mapper[ASCII_NUM];

int dx[DIR_NUM] = {0, 1, -1,  0};
int dy[DIR_NUM] = {1, 0,  0, -1};

bool InRange(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < n;
}

void Simulate() {
    while(t--) {
        int nx = x + dx[dir], ny = y + dy[dir];
        // 범위 안에 들어온다면 그대로 진행합니다.
        if(InRange(nx, ny)) {
            x = nx, y = ny;
        }
        // 벽에 부딪힌다면, 방향을 바꿔줍니다.
        else
            dir = 3 - dir;
    }
}

int main() {
    // 입력
    cin >> n >> t;
    
    // 각 알파벳 별 방향 번호를 설정합니다.
    mapper['R'] = 0;
    mapper['D'] = 1;
    mapper['U'] = 2;
    mapper['L'] = 3;
    
    char c_dir;
    cin >> x >> y >> c_dir;
    x--; y--; dir = mapper[c_dir];
    
    Simulate();
    
    cout << x + 1 << " " << y + 1;
    return 0;
}
*/