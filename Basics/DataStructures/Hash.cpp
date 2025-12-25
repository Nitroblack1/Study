// Hash table은 키를 값에 매핑할 수 있는 구조인, 연관 배열 추가에 사용되는 자료 구조이다.
// Hash table은 Hash 함수를 사용하여 색인(Index, Key)을 버킷(bucket)이나 슬롯(slot)의 배열로 계산한다.

#include <iostream>
#include <cstring>
using namespace std;

#define MAX_KEY 64
#define MAX_DATA 128
#define MAX_TABLE 4096

struct HashEntry {              // 해시 테이블의 엔트리 구조체
    char key[MAX_KEY + 1];
    char data[MAX_DATA + 1];
};

HashEntry tb[MAX_TABLE];

unsigned long djb2_hash(const char* str) {
    unsigned long h = 5381;
    int c;

    while ((c = *str++)) {
        h = (((h << 5) + h) + c) % MAX_TABLE; // h * 33 + c
    }
    return h % MAX_TABLE;
}

bool find_key(const char* key, char* out_data) {
    unsigned long h = djb2_hash(key);
    int cnt = MAX_TABLE;

    while (tb[h].key[0] != 0 && cnt--) {
        if (strcmp(tb[h].key, key) == 0) {
            strcpy(out_data, tb[h].data);
            return true;
        }
        h = (h + 1) % MAX_TABLE; // linear probing
    }
    return false;
}

bool add_key(const char* key, const char* data) {
    unsigned long h = djb2_hash(key);

    while (tb[h].key[0] != 0) {
        if (strcmp(tb[h].key, key) == 0) {
            return false; // already exists
        }
        h = (h + 1) % MAX_TABLE;
    }
    strcpy(tb[h].key, key);
    strcpy(tb[h].data, data);
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T, N, Q;
    cin >> T;

    for (int test_case = 1; test_case <= T; test_case++) {
        memset(tb, 0, sizeof(tb));

        cin >> N;

        char k[MAX_KEY + 1];
        char d[MAX_DATA + 1];

        for (int i = 0; i < N; i++) {
            cin >> k >> d;
            add_key(k, d);
        }

        cout << "#" << test_case << "\n";

        cin >> Q;
        for (int i = 0; i < Q; i++) {
            char qk[MAX_KEY + 1];
            char out[MAX_DATA + 1];

            cin >> qk;

            if (find_key(qk, out)) {
                cout << out << "\n";
            } else {
                cout << "not find\n";
            }
        }
    }
    return 0;
}
