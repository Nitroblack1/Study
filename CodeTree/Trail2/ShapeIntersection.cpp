#include <iostream>

using namespace std;

int x1, x2, x3, x4;

int main() {
    cin >> x1 >> x2 >> x3 >> x4;

    if ((x1 <= x3 && x2 >= x3) || (x3 <= x1 && x4 >= x1)) cout << "intersecting";
    else cout << "nonintersecting";

    return 0;
}

/*
#include <iostream>

using namespace std;

int x1, y1, x2, y2;
int a1, b1, a2, b2;

int main() {
    cin >> x1 >> y1 >> x2 >> y2;
    cin >> a1 >> b1 >> a2 >> b2;

    if (x2 < a1 || a2 < x1 || y2 < b1 || b2 < y1) cout << "nonoverlapping";
    else cout << "overlapping";

    return 0;
}
*/

/*
#include <iostream>
#include <algorithm>
#include <climits>

#define MAX_N 100

using namespace std;

int n;
int x1[MAX_N], x2[MAX_N];
bool ans = false;

int main() {
    // 입력
    cin >> n;
    for(int i = 0; i < n; i++)
        cin >> x1[i] >> x2[i];
    
    // 모든 선분을 한번씩 지어 보고, 모든 상황에 대해
    // 전부 겹치는 지점을 하나라도 만들 수 있는지 판단합니다.
    for(int skip = 0; skip < n; skip++) {
        int max_x1 = 0;
        int min_x2 = INT_MAX;
        bool possible = false;
        for(int i = 0; i < n; i++) {
            if(i == skip) continue;

            // 시작점 중 가장 뒤에 있는 좌표와 끝점 중 가장 앞에 있는 점의 좌표를 확인합니다.
            max_x1 = max(max_x1, x1[i]);
            min_x2 = min(min_x2, x2[i]);
        }

        // 만약 어느 한 선분이라도 시작점이 다른 선분의 끝점보다 뒤에 온다면
        // 선분이 전부 겹칠 수 없습니다.
        if(min_x2 >= max_x1)
            possible = true;
        else
            possible = false;
        
        // 만약 한 가지 방법이라도 전부 겹치는 지점을 만들 수 있다면,
        // 하나의 선분을 적절하게 제거했을 때 전부 겹칠수 있다는 것이 되므로 할 수 있게 됩니다.
        if(possible)
            ans = true;
    }

    if(ans)
        cout << "Yes";
    else
        cout << "No";

    return 0;
}
*/