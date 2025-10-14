#include <iostream>
#include <queue>
using namespace std;

int hanoi(int n, int start, int end, int via, queue<string>& result) {
    if (n <= 1) {
        result.push(to_string(start) + " " + to_string(end));
        return 1;
    }

    int count = 0;
    count += hanoi(n-1, start, via, end, result);

    count += 1;
    result.push(to_string(start) + " " + to_string(end));

    count += hanoi(n-1, via, end, start, result);

    return count;
}


int main() {
    int n;
    cin >> n;
    int start = 1;
    int via = 2;
    int end = 3;
    queue<string> result;
    int total = hanoi(n, start, end, via, result);
    cout << total << '\n';

    while (!result.empty()) {
        cout << result.front() << '\n';
        result.pop();
    }
}