#include <iostream>
#include <tuple>
#include <utility>  // To use pair
using namespace std;

class Student {
    public:
        int kor, eng, math;

        Student(int kor = 0, int eng = 0, int math = 0) {   // 인자 값이 없을 경우 0으로 초기화
            this->kor = kor;
            this->eng = eng;
            this->math = math;
        }
};

#include <iostream>
#include <string>

using namespace std;

string user2_id;
int user2_level;

/*
class User {
    public:
        string id;
        int level;

        User(string id, int level) {
            this->id = id;
            this->level = level;
        }

        void PrintUserInfo() {
            cout << "user " << this->id << " lv " << this->level << endl;
        }
};

int main() {
    cin >> user2_id >> user2_level;

    // Please write your code here.
    User user1 = User("codetree", 10);
    User user2 = User(user2_id, user2_level);

    user1.PrintUserInfo();
    user2.PrintUserInfo();

    return 0;
}
*/

/*
class Student {
    public:
        int kor, eng, math;

        Student(int kor, int eng, int math) {
            this->kor = kor;
            this->eng = eng;
            this->math = math;
        }

        Student() {}    // 인자가 없는 생성자 선언
};

Student students[5];
*/

/*
#include <iostream>
#include <string>
#define MAX_N 100

using namespace std;

int n;
string date, day, weather;

class Info {
    public:
        string d;
        string y;
        string w;

        Info(string d = "", string y = "", string w = "") {
            this->d = d;
            this->y = y;
            this->w = w;
        }
};

int main() {

    Info info[MAX_N];
    Info answer;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> date >> day >> weather;
        info[i] = Info(date, day, weather);
    }

    // Please write your code here.
    for (int i = 0; i < n; i++) {
        if (info[i].w == "Rain") {
            if (answer.w != "Rain") {
            answer = info[i];
            }
            else if (info[i].d < answer.d) answer = info[i];
        }
    }

    cout << answer.d << " " << answer.y << " " << answer.w;
    return 0;
}
*/

int main() {
    Student student1 = Student(90, 80, 90);
    Student student2 = Student();   // 0 0 0으로 초기화됨.
    cout << student1.kor << endl;
    cout << student1.eng << endl;
    cout << student1.math << endl;

    // Tuple example
    tuple<int, int, int> t = make_tuple(30, 15, 40);

    // How to get value from Tuple
    // 1. use 'get' function
    int v1 = get<0>(t);
    int v2 = get<1>(t);
    int v3 = get<2>(t);

    // 2. use 'tie' function
    int v1, v2, v3;
    tie(v1, v2, v3) = t;    // v1 : 30, v2 : 15, v3 : 40
    tie(v1, ignore, ignore) = t;    // v1 : 30 만 대입.

    // tuple을 사용할 때 각 값이 무엇을 의미하는 지 알기 어렵기 때문에
    // 값을 이용할 때 되도록 tuple 값을 받아 줄 변수에 꼭 적절한 이름을 붙여준 뒤 사용하는 것을 권장한다.
    cout << get<0>(t);  // 30
    get<1>(t) = 50;  // t의 두 번째 요소가 50으로 변경됨.
    t = make_tuple(0, 0, 90);   // tuple 의미상 변경보단 새로 만들자.

    int kor, eng, math;
    tie(kor, eng, math) = t;
    cout << kor << " " << eng << " " << math;   // 30 50 40

    // pair -> need '#include <utility>'
    // tuple과 달리 pair는 정확히 2개 숫자만 담을 수 있다.
    // 접근시 .first, .second 로 접근이 가능하며, 값 변경 역시 간단하다.
    pair<int, int> p = make_pair(1, 5);
    cout << p.first << endl;    // 1
    cout << p.second << endl;   // 5
    p.first = 10;
    p.second = 52;
    cout << p.first << endl;    // 10
    cout << p.second << endl;   // 52
}