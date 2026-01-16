#include <iostream>

#define MAX_N 100
#define MAX_R 2000
#define OFFSET 1000

using namespace std;

int n;
int x1[MAX_N], x2[MAX_N];

int checked[MAX_R + 1];

int main() {
    // 입력
    cin >> n;
    
	// 현재 위치
	int cur = 0;
	
    for(int i = 0; i < n; i++) {
		int distance;
		char direction;
        cin >> distance >> direction;
		
		if(direction == 'L') {
			// 왼쪽으로 이동할 경우 : cur - distance ~ cur까지 경로 이동
			x1[i] = cur - distance;
			x2[i] = cur;
			cur -= distance;
		}
		else {
			// 오른쪽으로 이동할 경우 : cur ~ cur + distance까지 경로 이동
			x1[i] = cur;
			x2[i] = cur + distance;
			cur += distance;
		}
        
        // OFFSET을 더해줍니다.
        x1[i] += OFFSET;
        x2[i] += OFFSET;
    }
    
    // 구간을 칠해줍니다.
    // 구간 단위로 진행하는 문제이므로
    // x2[i]에 등호가 들어가지 않음에 유의합니다.
    for(int i = 0; i < n; i++)
        for(int j = x1[i]; j < x2[i]; j++)
            checked[j]++;
    
    // 2번 이상 지나간 영역의 크기를 구합니다.
    int cnt = 0;
    for(int i = 0; i <= MAX_R; i++)
        if(checked[i] >= 2)
            cnt++;
    
    cout << cnt;
    return 0;
}

/*
#include <iostream>

using namespace std;

int n;
int x[100];
char dir[100];
int road[2001];
int curPos = 1000;

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> x[i] >> dir[i];
    }

    for (int i = 0; i < n; i++) {
        if (dir[i] == 'L') {
            for (int j = curPos - 1; j >= curPos - x[i]; j--) {
                road[j]++;
            }
            curPos -= x[i];
        } else {
            for (int j = curPos; j < curPos + x[i]; j++) {
                road[j]++;
            }
            curPos += x[i];
        }
    }

    int count = 0;
    for (int i = 1; i < 2000; i++) {
        if (road[i] >= 2) count++;
    }

    cout << count;

    return 0;
}
*/

/*
#include <iostream>
using namespace std;

int n;
int x[1000];
char dirArr[1000];

int wCnt[200000];   // 흰색 칠한 횟수 (0~2 cap)
int bCnt[200000];   // 검은색 칠한 횟수 (0~2 cap)
int state[200000];  // 0: 미칠, 1: 흰, 2: 검, 3: 회색(고정)

int curPos = 100000;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x[i] >> dirArr[i];
    }

    for (int i = 0; i < n; i++) {
        int dis = x[i];
        char d = dirArr[i];

        if (d == 'L') {
            // curPos 포함 dis칸: curPos .. curPos-(dis-1)
            for (int p = curPos; p >= curPos - (dis - 1); p--) {
                if (state[p] == 3) continue;

                if (wCnt[p] < 2) wCnt[p]++;
                if (wCnt[p] >= 2 && bCnt[p] >= 2) {
                    state[p] = 3;
                } else {
                    state[p] = 1; // 마지막 색: 흰
                }
            }
            curPos -= (dis - 1);  // 마지막으로 칠한 타일
        } else { // 'R'
            // curPos 포함 dis칸: curPos .. curPos+(dis-1)
            for (int p = curPos; p <= curPos + (dis - 1); p++) {
                if (state[p] == 3) continue;

                if (bCnt[p] < 2) bCnt[p]++;
                if (wCnt[p] >= 2 && bCnt[p] >= 2) {
                    state[p] = 3;
                } else {
                    state[p] = 2; // 마지막 색: 검
                }
            }
            curPos += (dis - 1);
        }
    }

    int w = 0, b = 0, g = 0;
    for (int i = 0; i < 200000; i++) {
        if (state[i] == 1) w++;
        else if (state[i] == 2) b++;
        else if (state[i] == 3) g++;
    }

    cout << w << " " << b << " " << g;
    return 0;
}

*/

/*
#include <iostream>

using namespace std;

#define MAX_K 100000

int n;
int a[2 * MAX_K + 1];
int cnt_b[2 * MAX_K + 1];
int cnt_w[2 * MAX_K + 1];
int b, w, g;

int main() {
    // 변수 입력
    cin >> n;

    int cur = MAX_K;

    for(int i = 1; i <= n; i++) {
        int x;
        char c;
        cin >> x >> c;
        if(c == 'L') {
            // x칸 왼쪽으로 칠합니다.
            while(x--) {
                a[cur] = 1;
                cnt_w[cur]++;
                if(x) cur--;
            }
        }
        else {
            // x칸 오른쪽으로 칠합니다.
            while(x--) {
                a[cur] = 2;
                cnt_b[cur]++;
                if(x) cur++;
            }
        }
    }

    for(int i = 0; i <= 2 * MAX_K; i++) {
        // 검은색과 흰색으로 두 번 이상 칠해진 타일은 회색입니다.
        if(cnt_b[i] >= 2 && cnt_w[i] >= 2) g++;
        // 그렇지 않으면 현재 칠해진 색깔이 곧 타일의 색깔입니다.
        else if(a[i] == 1) w++;
        else if(a[i] == 2) b++;
    }

    // 정답을 출력합니다.
    cout << w << " " << b << " " << g;
    return 0;
}
*/