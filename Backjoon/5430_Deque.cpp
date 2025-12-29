#include <iostream>
#include <deque>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;

    while (T--) {
        string p;
        cin >> p;

        int n;
        cin >> n;

        string arr_str;
        cin >> arr_str;

        deque<int> dq;
        string num = "";
        for (int i = 1; i < arr_str.size(); i++) {
            if (isdigit(arr_str[i])) {
                num += arr_str[i];
            } else {
                if (!num.empty()) {
                    dq.push_back(stoi(num));
                    num = "";
                }
            }
        }

        bool is_reversed = false;
        bool error = false;

        for (char cmd : p) {
            if (cmd == 'R') {
                is_reversed = !is_reversed;
            } else if (cmd == 'D') {
                if (dq.empty()) {
                    error = true;
                    break;
                }
                if (is_reversed) {
                    dq.pop_back();
                } else {
                    dq.pop_front();
                }
            }
        }

        if (error) {
            cout << "error\n";
        } else {
            cout << "[";
            if (is_reversed) {
                for (int i = dq.size() - 1; i >= 0; i--) {
                    cout << dq[i];
                    if (i != 0) cout << ",";
                }
            } else {
                for (int i = 0; i < dq.size(); i++) {
                    cout << dq[i];
                    if (i != dq.size() - 1) cout << ",";
                }
            }
            cout << "]\n";
        }
    }

    return 0;
}