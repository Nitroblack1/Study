#include <iostream>
#include <sstream>
#include <deque>
#include <vector>
#include <string>
#include <algorithm> // for any_of
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    cin.ignore();

    vector<deque<string>> parrots(n);

    for (int i = 0; i < n; ++i) {
        string line, word;
        getline(cin, line);
        stringstream ss(line);
        while (ss >> word) parrots[i].push_back(word);
    }

    string line, word;
    getline(cin, line);
    stringstream ss(line);
    deque<string> target;
    while (ss >> word) target.push_back(word);

    // 메인 로직
    while (!target.empty()) {
        bool matched = false;

        for (auto &p : parrots) {
            if (!p.empty() && p.front() == target.front()) {
                p.pop_front();
                target.pop_front();
                matched = true;
                break;
            }
        }

        if (!matched) {
            cout << "Impossible";
            return 0;
        }
    }

    // 아직 말 안 끝낸 앵무새가 있다면 Impossible
    bool remain = any_of(parrots.begin(), parrots.end(),
                         [](const deque<string>& p) { return !p.empty(); });

    cout << (remain ? "Impossible" : "Possible");
    return 0;
}
