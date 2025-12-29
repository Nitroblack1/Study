#include <iostream>
#include <string>
#include <vector>
#include <functional>
using namespace std;

class HashTable {
private:
    static constexpr size_t TABLE_SIZE = 4096;

    struct Entry {
        string key;
        string value;
        bool occupied = false;   // 현재 이 슬롯이 사용 중인가?
    };

    vector<Entry> table;

    size_t hashKey(const string& key) const {
        return std::hash<string>{}(key) % TABLE_SIZE;
    }

public:
    HashTable() : table(TABLE_SIZE) {}

    void clear() {
        for (auto& e : table) e = Entry{};
    }

    // key 존재하면 value를 out에 넣고 true
    bool find(const string& key, string& out) const {
        size_t h = hashKey(key);
        size_t cnt = TABLE_SIZE;

        while (table[h].occupied && cnt--) {
            if (table[h].key == key) {
                out = table[h].value;
                return true;
            }
            h = (h + 1) % TABLE_SIZE;
        }
        return false;
    }

    // key 없으면 삽입하고 true, 이미 있으면 false
    bool insert(const string& key, const string& value) {
        size_t h = hashKey(key);
        size_t cnt = TABLE_SIZE;

        while (table[h].occupied && cnt--) {
            if (table[h].key == key) return false; // already exists
            h = (h + 1) % TABLE_SIZE;
        }

        if (cnt == 0) return false; // 테이블이 꽉 찼거나 비정상

        table[h].key = key;
        table[h].value = value;
        table[h].occupied = true;
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    HashTable ht;

    for (int tc = 1; tc <= T; tc++) {
        ht.clear();

        int N;
        cin >> N;

        for (int i = 0; i < N; i++) {
            string k, d;
            cin >> k >> d;
            ht.insert(k, d);
        }

        cout << "#" << tc << "\n";

        int Q;
        cin >> Q;
        for (int i = 0; i < Q; i++) {
            string qk, out;
            cin >> qk;

            if (ht.find(qk, out)) cout << out << "\n";
            else cout << "not find\n";
        }
    }
    return 0;
}