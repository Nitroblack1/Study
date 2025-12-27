#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <functional>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, v;
    cin >> n >> m >> v;

    // adjacency list로 그래프 표현
    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    // 정점 번호가 작은 것부터 방문하기 위해 정렬
    for (int i = 1; i <= n; i++) {
        sort(adj[i].begin(), adj[i].end());
    }

    // DFS
    vector<bool> visited(n + 1, false);
    function<void(int)> dfs = [&](int u) {
        visited[u] = true;
        cout << u << ' ';
        for (int V : adj[u]) {
            if (!visited[V]) {
                dfs(V);
            }
        }
    };

    dfs(v);
    cout << '\n';

    // BFS
    fill(visited.begin(), visited.end(), false);
    queue<int> q;
    q.push(v);
    visited[v] = true;

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        cout << u << ' ';
        for (int v : adj[u]) {
            if (!visited[v]) {
                visited[v] = true;
                q.push(v);
            }
        }
    }
    cout << '\n';

    return 0;
}