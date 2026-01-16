#include <iostream>
using namespace std;

int x1[2], y1[2];
int x2[2], y2[2];
int grid[2001][2001];

int main() {
    cin >> x1[0] >> y1[0] >> x2[0] >> y2[0];
    cin >> x1[1] >> y1[1] >> x2[1] >> y2[1];

    for (int i = x1[0] + 1000; i < x2[0] + 1000; i++) {
        for (int j = y1[0] + 1000; j < y2[0] + 1000; j++) {
            grid[i][j] = 1;
        }
    }

    for (int i = x1[1] + 1000; i < x2[1] + 1000; i++) {
        for (int j = y1[1] + 1000; j < y2[1] + 1000; j++) {
            grid[i][j] = 0;
        }
    }

    int lx = -1, rx = -1, uy = -1, dy = -1;
    for (int i = 0; i <= 2000; i++) {
        for (int j = 0; j <= 2000; j++) {
            if (grid[i][j] == 1) {
                if (lx == -1) { // 첫 발견
                    lx = rx = i;
                    dy = uy = j;
                } else {
                    if (i < lx) lx = i;
                    if (i > rx) rx = i;
                    if (j < dy) dy = j;
                    if (j > uy) uy = j;
                }
            }
        }
    }

    if (lx == -1) {
        cout << 0;
    } else {
        int width  = rx - lx + 1;
        int height = uy - dy + 1;
        cout << width * height;
    }

    return 0;
}

/*
#include <iostream>

using namespace std;

int N;
int x1, x2, y1, y2;
int grid[201][201];

int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> x1 >> y1 >> x2 >> y2;

        for (int row = x1 + 100; row < x2 + 100; row++) {
            for (int col = y1 + 100; col < y2 + 100; col++) {
                grid[row][col] = 1;
            }
        }
    }

    int area = 0;
    for (int r = 0; r <= 200; r++) {
        for (int c = 0; c <= 200; c++) {
            area += grid[r][c];
        }
    }

    cout << area;

    return 0;
} */

/*
#include <iostream>
#define l 8

using namespace std;

int N;
int x, y, area;
int grid[201][201];

int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> x >> y;
        for (int i = x + 100; i < x + 100 + l; i++) {
            for (int j = y + 100; j < y + 100 + l; j++) {
                grid[i][j] = 1;
            }
        }
    }

    for (int i = 0; i <= 200; i++) {
        for (int j = 0; j <= 200; j++) {
            area += grid[i][j];
        }
    }

    cout << area;

    return 0;
}
*/

