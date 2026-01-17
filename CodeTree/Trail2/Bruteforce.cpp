// #include <iostream>
// #include <cstdlib>
// #include <algorithm>
// using namespace std;

// int n = 4;
// int arr[4] = {1, 5, 2, 6};

// // 4C2
// int main() {
//     int max_sum = 0;
//     for(int i = 0; i < n; i++)
//         for(int j = i + 1; j < n; j++) {
//             arr[i] *= 2;
//             arr[j] *= 2;
    
//             int sum_diff = 0;
//             for(int k = 0; k < n - 1; k++)
//                 sum_diff += abs(arr[k + 1] - arr[k]);
    
//             max_sum = max(max_sum, sum_diff);
//             arr[i] /= 2;
//             arr[j] /= 2;
//         }    
//     cout << max_sum;
    
//     return 0;
// }


// 4C3
// #include <iostream>
// #include <cstdlib>
// #include <algorithm>
// using namespace std;

// int n = 4;
// int arr[4] = {1, 5, 2, 6};

// int main() {
//     int max_sum = 0;
//     for(int i = 0; i < n; i++)
//         for(int j = i + 1; j < n; j++)
//             for(int k = j + 1; k < n; k++) {
//                 arr[i] *= 2;
//                 arr[j] *= 2;
//                 arr[k] *= 2;
    
//                 int sum_diff = 0;
//                 for(int l = 0; l < n - 1; l++)
//                     sum_diff += abs(arr[l + 1] - arr[l]);
    
//                 max_sum = max(max_sum, sum_diff);
//                 arr[i] /= 2;
//                 arr[j] /= 2;
//                 arr[k] /= 2;
//             }
    
//     cout << max_sum;
    
//     return 0;
// }

#include <iostream>

using namespace std;

int R, C;
char grid[15][15];
char color;
int jump1, jump2;

int main() {
    cin >> R >> C;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            cin >> grid[i][j];
        }
    }

    if (grid[0][0] == grid[R-1][C-1]) {
        cout << 0;
        return 0;
    }

    int total = 0;
    for (int i = 1; i < R - 2; i++) {
        for (int j = 1; j < C - 2; j++) {
            if (grid[0][0] != grid[i][j]) {
                jump1++;
                for (int k = i + 1; k < R - 1; k++) {
                    for (int l = j + 1; l < C - 1; l++) {
                        if (grid[0][0] == grid[k][l]) {
                            jump2++;
                        }
                    }
                }
                total += jump1 * jump2;
                jump1 = 0;
                jump2 = 0;
            }
        }
    }

    cout << total;

    return 0;
}

/*
#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

int abilities[6];

int GetDiff(int p1, int p2, int p3) {
    int team2 = 0;
    int team1 = abilities[p1] + abilities[p2] + abilities[p3];

    for (int i = 0; i < 6; i++) {
        team2 += abilities[i];
    }

    team2 -= team1;
    
    return abs(team1 - team2);
}

int main() {
    int answer = INT_MAX;

    for (int i = 0; i < 6; i++) {
        cin >> abilities[i];
    }

    for (int i = 0; i < 4; i++) {
        for (int j = i + 1; j < 5; j++) {
            for (int k = j + 1; k < 6; k++) {
                answer = min(GetDiff(i, j, k), answer);
            }
        }
    }

    cout << answer;

    return 0;
}
*/

/*
#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

int arr[5];

int GetDiff(int p1, int p2, int p3) {
    int team1 = arr[p1];
    int team2 = arr[p2] + arr[p3];

    int team3 = 0;
    for (int i = 0; i < 5; i++) team3 += arr[i];
    team3 = team3 - team1 - team2;

    if (team1 == team2 || team2 == team3 || team1 == team3) return -1;

    int mx = max(team1, max(team2, team3));
    int mn = min(team1, min(team2, team3));
    return mx - mn;
}

int main() {
    int minGap = INT_MAX;

    for (int i = 0; i < 5; i++) cin >> arr[i];

    bool isPossible = false;

    for (int p1 = 0; p1 < 5; p1++) {
        for (int p2 = 0; p2 < 5; p2++) {
            if (p2 == p1) continue;
            for (int p3 = 0; p3 < 5; p3++) {
                if (p3 == p1 || p3 == p2) continue;
                int curGap = GetDiff(p1, p2, p3);
                if (curGap == -1) continue;
                minGap = min(minGap, curGap);
                isPossible = true;
            }
        }
    }

    cout << (isPossible ? minGap : -1);
    return 0;
}
*/