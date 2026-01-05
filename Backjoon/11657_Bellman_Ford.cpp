#include <iostream>
#include <vector>
#include <limits>

using namespace std;

struct Edge {
    int from;
    int to;
    long long w;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<Edge> edges;
    edges.reserve(M);

    for (int i = 0; i < M; i++) {
        int A, B;
        long long C;
        cin >> A >> B >> C;
        edges.push_back({A, B, C});
    }

    const long long INF = (1LL << 60);
    vector<long long> dist(N + 1, INF);
    dist[1] = 0;

    // Bellman-Ford: relax edges N-1 times
    for (int i = 1; i <= N - 1; i++) {
        bool updated = false;
        for (const auto &e : edges) {               // 참조를 안쓰면 매 반복마다 객체 복사 비용이 발생한다.
            if (dist[e.from] == INF) continue;      // 참조를 통해 edge[i]를 직접 가리키게 함으로서 위 비용을 줄일 수 있다.
            if (dist[e.to] > dist[e.from] + e.w) {
                dist[e.to] = dist[e.from] + e.w;
                updated = true;
            }
        }
        if (!updated) break; // early stop
    }

    // One more iteration to detect negative cycle reachable from 1
    for (const auto &e : edges) {
        if (dist[e.from] == INF) continue;
        if (dist[e.to] > dist[e.from] + e.w) {
            cout << -1 << "\n";
            return 0;
        }
    }

    for (int i = 2; i <= N; i++) {
        if (dist[i] == INF) cout << -1 << "\n";
        else cout << dist[i] << "\n";
    }

    return 0;
}
