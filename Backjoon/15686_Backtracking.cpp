#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

struct Pos {
    int r, c;
};

int main() {
    int N, M;
    cin >> N >> M;

    vector<Pos> houses;
    vector<Pos> chickens;

    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            int value;
            cin >> value;
            if (value == 1) {
                houses.push_back({r, c});
            } else if (value == 2) {
                chickens.push_back({r, c});
            }
        }
    }

    int C = (int)chickens.size();
    vector<bool> select(C, false);

    for (int i = C - M; i < C; i++) select[i] = true;

    int answer = INT32_MAX;

    do {
        int cityDist = 0;

        for (const auto& h : houses) {
            int best = INT32_MAX;
            for (int i = 0; i < C; i++) {
                if (!select[i]) continue;
                int d = abs(h.r - chickens[i].r) + abs(h.c - chickens[i].c);
                if (d < best) best = d;
            }
            cityDist += best;
            if (cityDist >= answer) break;
        }
        if (cityDist < answer) answer = cityDist;

    } while (next_permutation(select.begin(), select.end()));

    cout << answer << '\n';
    return 0;
}