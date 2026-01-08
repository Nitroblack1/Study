#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static long long countDisks(const vector<int>& a, long long cap) {
    long long cnt = 1;
    long long sum = 0;

    for (int x : a) {
        if (sum + x <= cap) {
            sum += x;
        } else {
            cnt++;
            sum = x;
        }
    }
    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<int> a(N);
    long long lo = 0;      // 최소 가능한 용량 (최대 레슨 길이)
    long long hi = 0;      // 최대 가능한 용량 (전체 합)

    for (int i = 0; i < N; i++) {
        cin >> a[i];
        lo = max(lo, (long long)a[i]);
        hi += a[i];
    }

    long long ans = hi;

    while (lo <= hi) {
        long long mid = (lo + hi) / 2;  // 블루레이 용량 후보
        long long need = countDisks(a, mid);

        if (need <= M) {        // 가능한 용량 -> 더 줄여보기
            ans = mid;
            hi = mid - 1;
        } else {                // 불가능 -> 더 키우기
            lo = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}