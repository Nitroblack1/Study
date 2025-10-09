#include <iostream>
#include <deque>
#include <sstream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T;
    cin >> T;

    while(T--) {
        int n, target;
        cin >> n >> target;
        cin.ignore();

        string line;
        getline(cin, line);

        stringstream ss(line);
        deque<int> dq, order;
        int x;
        int ans = 1;

        int idx = 0;
        while (ss >> x) {
            dq.push_back(x);
            order.push_back(idx++);
        }

        int targetNum = order.at(target);

        while (dq.size() != 0) {
            bool flag = false;
            for (int i = 1; i < dq.size(); i++) {
                if (dq.front() < dq.at(i)) {
                    dq.push_back(dq.front());
                    dq.pop_front();

                    order.push_back(order.front());
                    order.pop_front();
                    flag = true;
                    break;
                }
            }
        
            if (!flag) {
                if (targetNum == order.front()) {
                    cout << ans << '\n';
                    break;
                } else {
                    dq.pop_front();
                    order.pop_front();
                    ans++;
                }
            }
        }
    }
}