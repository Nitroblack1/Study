// #include <iostream>
// #include <algorithm>

// using namespace std;

// class Student {
//     public:
//         int kor, eng, math;

//         Student(int kor, int eng, int math) {
//             this->kor = kor;
//             this->eng = eng;
//             this->math = math;
//         }
// };

// bool cmp(const Student &a, const Student &b) { // 국어 점수 기준 내림차순 정렬
//     return a.kor > b.kor;   // '작은 것이 앞에 온다' 가 false
// }

// bool cmp(const Student &a, const Student &b) { // 국어 점수 기준 오름차순 정렬
//     return a.kor < b.kor;   // '작은 것이 앞에 온다' 가 true
// }

// bool cmp(const Student &a, const Student &b) { 
//     if(a.kor == b.kor)           // 국어 점수가 일치한다면
//         return a.eng < b.eng;    // 영어 점수를 기준으로 오름차순 정렬합니다.
//     return a.kor < b.kor;        // 국어 점수가 다르다면, 오름차순 정렬합니다.
// }

// bool cmp(Student a, Student b) { 
//     return make_tuple(a.kor, a.eng) < make_tuple(b.kor, b.eng);     // 국어 오름차순 -> 영어 오름차순
// }

// bool cmp(Student a, Student b) { 
//     return make_tuple(a.kor, -a.eng) < make_tuple(b.kor, -b.eng);   // 국어 오름차순 -> 영어 내림차순
// }


// /*
// int main() {
//     Student students[5] = {
//         Student(90, 80, 90), // 첫 번째 학생
//         Student(20, 80, 80), // 두 번째 학생
//         Student(90, 30, 60), // 세 번째 학생
//         Student(60, 10, 50), // 네 번째 학생
//         Student(80, 20, 10)  // 다섯 번째 학생 
//     };

//     sort(students, students + 5, cmp); // 국어 점수 기준 내림차순 정렬

//     for(int i = 0; i < 5; i++)
//         cout << students[i].kor << " " << students[i].eng << " " << students[i].math << endl;

//     return 0;
// }

// >> 90 80 90
//    90 30 60
//    80 20 10
//    60 10 50
//    20 80 80
// */

// #include <iostream>
// #include <string>
// #include <algorithm>

// using namespace std;

// int n;
// string name;
// int korean;
// int english;
// int math;

// class Student {
//     public:
//         string n;
//         int k;
//         int e;
//         int m;

//         Student (string n = "", int k = 0, int e = 0, int m = 0) {
//             this->n = n;
//             this->k = k;
//             this->e = e;
//             this->m = m;
//         }
// };

// bool cmp(const Student &a, const Student &b) {
//     if (a.k == b.k && a.e == b.e) {
//         return a.m > b.m;
//     } else if (a.k == b.k) {
//         return a.e > b.e;
//     } else {
//         return a.k > b.k;
//     }
// }

// int main() {
//     cin >> n;
//     Student student[10];

//     for (int i = 0; i < n; i++) {
//         cin >> name;
//         cin >> korean;
//         cin >> english;
//         cin >> math;

//         student[i] = Student(name, korean, english, math);
//     }

//     // sort(student, student + n, cmp);

//     for (int i = 0; i < n; i++) {
//         cout << student[i].n << " " << student[i].k << " " << student[i].e << " " << student[i].m << endl;
//     }

//     return 0;
// }