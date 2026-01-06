#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;

        vector<int> parent(N + 1, 0);

        for (int i = 0; i < N - 1; i++) {
            int p, c;
            cin >> p >> c;
            parent[c] = p;
        }

        int a, b;
        cin >> a >> b;

        vector<char> visited(N + 1, 0);
        int x = a;
        while (x != 0) {
            visited[x] = 1;
            x = parent[x];
        }

        int y = b;
        while (!visited[y]) {
            y = parent[y];
        }

        cout << y << '\n';
    }

    return 0;
}