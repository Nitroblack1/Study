#include <iostream>
#include <vector>
#include <limits>

using namespace std;

static const int N = 100;
static const int INF = 100000;

int mp[N + 1][N + 1];
int visitArr[N + 1];
int distArr[N + 1];
int vertex, edge, startV, endV;

void dijkstra() {
    distArr[startV] = 0;

    for (int i = 1; i <= vertex; i++) {
        int mn = INF;
        int v = -1;

        // 방문 안 했고 dist가 최소인 정점 선택
        for (int j = 1; j <= vertex; j++) {
            if (visitArr[j] == 0 && mn > distArr[j]) {
                mn = distArr[j];
                v = j;
            }
        }

        // 더 이상 갈 수 있는 정점이 없으면 종료(안전장치)
        if (v == -1) break;

        visitArr[v] = 1;

        // v를 거쳐서 가는 경로로 완화
        for (int j = 1; j <= vertex; j++) {
            if (distArr[v] + mp[v][j] < distArr[j]) {
                distArr[j] = distArr[v] + mp[v][j];
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    for (int test_case = 1; test_case <= T; test_case++) {
        cin >> vertex >> startV >> endV;
        cin >> edge;

        // 인접행렬 초기화
        for (int i = 1; i <= vertex; i++) {
            for (int j = 1; j <= vertex; j++) {
                if (i == j) mp[i][j] = 0;
                else mp[i][j] = INF;
            }
        }

        // 간선 입력
        for (int i = 1; i <= edge; i++) {
            int from, to, value;
            cin >> from >> to >> value;
            mp[from][to] = value;
        }

        // dist/visit 초기화
        for (int i = 1; i <= vertex; i++) {
            distArr[i] = INF;
            visitArr[i] = 0;
        }

        dijkstra();

        cout << "#" << test_case << " " << distArr[endV] << "\n";
    }

    return 0;
}