#include <iostream>
#include <vector>

using namespace std;

int N, R, Q;
vector<vector<int>> adj;
vector<int> subSize;

int dfs(int u, int parent) {
    subSize[u] = 1;
    for (int v : adj[u]) {
        if (v != parent) {
            subSize[u] += dfs(v, u);
        }
    }
    return subSize[u];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> R >> Q;
    adj.assign(N + 1, {});
    subSize.assign(N + 1, 0);

    for (int i = 0; i < N - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(R, 0);

    for (int i = 0; i < Q; i++) {
        int u;
        cin >> u;
        cout << subSize[u] << '\n';
    }

    return 0;
}