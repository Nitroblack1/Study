#include <iostream>

using namespace std;

int m1, d1, m2, d2;

void GetDay(int m1, int d1, int m2, int d2) {
    int month[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    string day[7] = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"};
    int diff = 0;

    bool reverse = (m1 > m2) ? true : (m1 == m2 && d1 > d2) ? true : false;

    if (reverse) {
        for (int i = 1; i < m1; i++) {
            diff += month[i];
        }
        diff += d1;

        for (int i = 1; i < m2; i++) {
            diff -= month[i];
        }
        diff -= d2;

        cout << day[7 - diff % 7];
    } else {
        for (int i = 1; i < m2; i++) {
            diff += month[i];
        }
        diff += d2;

        for (int i = 1; i < m1; i++) {
            diff -= month[i];
        }
        diff -= d1;

        cout << day[diff % 7];
    }
}

int main() {
    cin >> m1 >> d1 >> m2 >> d2;

    // Please write your code here.
    GetDay(m1, d1, m2, d2);

    return 0;
}

/*
#include <iostream>
#include <string>

using namespace std;

int NumOfDays(int m, int d) {
    // 계산 편의를 위해 월마다 몇 일이 있는지를 적어줍니다. 
    int days[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int total_days = 0;
    
    // 1월부터 (m - 1)월 까지는 전부 꽉 채워져 있습니다.
    for(int i = 1; i < m; i++)
        total_days += days[i];
    
    // m월의 경우에는 정확이 d일만 있습니다.
    total_days += d;
    
    return total_days;
}

int main() {
    // 변수 선언 및 입력
    int m1, m2, d1, d2;
    cin >> m1 >> d1 >> m2 >> d2;
    
    // 두 날짜간의 차이가 몇 일인지를 구합니다.
    int diff = NumOfDays(m2, d2) - NumOfDays(m1, d1);
    
    // 음수인 경우에는, 양수로 넘겨 계산해주면 올바르게 계산이 됩니다. 
    while(diff < 0)
        diff += 7;
    
    // 알맞은 요일의 이름을 출력합니다.
    string day_of_week[] = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"};
    cout << day_of_week[diff % 7];
    return 0;
}
*/

/*
#include <iostream>

using namespace std;

int m1, m2, d1, d2;
string A;

int month[13] = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
string days[7] = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"};

void GetDiff(int m1, int d1, int m2, int d2, string day) {
    int diff = 1;
    for (int i = 1; i < m2; i++) {
        diff += month[i];
    }
    diff += d2;

    for (int i = 1; i < m1; i++) {
        diff -= month[i];
    }
    diff -= d1;

    int bonus = 0;
    for (int i = 1; i < diff % 7; i++) {
        if (days[i] == day) {
            bonus = 1;
            break;
        }
    }

    cout << diff / 7 + bonus;
}

int main() {
    cin >> m1 >> d1 >> m2 >> d2;
    cin >> A;

    GetDiff(m1, d1, m2, d2, A);

    return 0;
}
*/