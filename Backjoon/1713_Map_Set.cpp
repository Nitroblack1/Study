#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class PhotoFrame {
public:
    int id;
    int count;
    int time;

    PhotoFrame(int id, int time) : id(id), count(1), time(time) {}

    void recommend() {
        count++;
    }

    bool operator<(const PhotoFrame& other) const {
        if (count != other.count) return count < other.count;
        return time < other.time;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, R;
    cin >> N >> R;

    vector<PhotoFrame> frames;

    for (int t = 0; t < R; t++) {
        int student;
        cin >> student;

        auto it = find_if(frames.begin(), frames.end(), 
            [&](const PhotoFrame& f) {return f.id == student; });

        if (it != frames.end()) {
            it->recommend();
            continue;
        }

        if ((int)frames.size() == N) {
            auto victim = min_element(frames.begin(), frames.end());
            frames.erase(victim);
        }
        frames.emplace_back(student, t);
    }

    sort(frames.begin(), frames.end(), 
        [](const PhotoFrame& a, const PhotoFrame& b) { return a.id < b.id; });

    for (const auto& frame : frames) {
        cout << frame.id << " ";
    }
    cout << "\n";
}