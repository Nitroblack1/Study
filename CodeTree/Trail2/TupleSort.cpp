#include <iostream>
#include <tuple>
#include <algorithm>
#define MAX_N 1000

using namespace std;

int N;
int h;
int w;

int main() {
    cin >> N;
    tuple<int, int, int> students[MAX_N];

    for (int i = 0; i < N; i++) {
        cin >> h >> w;
        students[i] = make_tuple(-h, -w, i + 1);
    }

    sort(students, students + N);

    int height, weight, id;
    for (int i = 0; i < N; i++) {
        tie(height, weight, id) = students[i];
        cout << -height << " " << -weight << " " << id << endl;
    }

    return 0;
}

/*
int n;
string name;
int score1;
int score2;
int score3;

bool cmp(const tuple<string, int, int, int> &a, const tuple<string, int, int, int> &b) {
    int a1, a2, a3;
    tie(ignore, a1, a2, a3) = a;
    int b1, b2, b3;
    tie(ignore, b1, b2, b3) = b;
    return a1 + a2 + a3 < b1 + b2 + b3;
}

int main() {
    cin >> n;
    tuple<string, int, int, int> students[10];

    for (int i = 0; i < n; i++) {
        cin >> name;
        cin >> score1;
        cin >> score2;
        cin >> score3;
        students[i] = make_tuple(name, score1, score2, score3);
    }

    // Please write your code here.
    sort(students, students + n, cmp);

    for (int i = 0; i < n; i++) {
        string n;
        int s1, s2, s3;
        tie(n, s1, s2, s3) = students[i];
        cout << n << " " << s1 << " " << s2 << " " << s3 << endl;
    }

    return 0;
}
*/

/*
int main() {
    tuple<int, int, int> students[5] = {
        make_tuple(90, 80, 90), // 첫 번째 학생
        make_tuple(20, 80, 80), // 두 번째 학생
        make_tuple(90, 30, 60), // 세 번째 학생
        make_tuple(60, 10, 50), // 네 번째 학생
        make_tuple(80, 20, 10), // 다섯 번째 학생 
    };

    tuple<int, int, int> students2[5] = {
        make_tuple(-90, 80, 90), // 첫 번째 학생
        make_tuple(-20, 80, 80), // 두 번째 학생
        make_tuple(-90, 30, 60), // 세 번째 학생
        make_tuple(-60, 10, 50), // 네 번째 학생
        make_tuple(-80, 20, 10), // 다섯 번째 학생 
    };

    sort(students2, students2 + 5); // 국어 점수 기준 내림차순 정렬, 마지막에 - 떼주면 끝.
    // string이나 char의 경우 사전 순으로 빠른 것부터 나타난다.
  
    for(int i = 0; i < 5; i++) {
        int kor, eng, math;
        tie(kor, eng, math) = students[i];
        cout << kor << " " << eng << " " << math << endl;
    }

    return 0;
}

>> 20 80 80
   60 10 50
   80 20 10
   90 30 60
   90 80 90
*/

