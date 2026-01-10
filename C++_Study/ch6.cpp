#include <iostream>

/*
구조체 (struct) : 여러 개의 변수를 하나로 묶어서 관리할 수 있는 사용자 정의 데이터 타입
*/

struct Date {
    int year;
    int month;
    int day;
} yesterday, today, tomorrow; // 구조체 변수 선언과 동시에 생성

int main() {
    Date holiday = {2026, 01, 01}; // 구조체 변수 선언과 동시에 초기화

    return 0;
}

/*
Class (클래스) : 구조체와 유사하지만, 멤버 변수와 멤버 함수(메서드)를 포함할 수 있는 사용자 정의 데이터 타입
*/

class DayOfYear {
    public:
    void output();
    int month;
    int day;
};

void DayOfYear::output() {
    // 멤버 함수 정의
    std::cout << "Month: " << month << ", Day: " << day << std::endl;
}
// :: (scope resolution operator) : 클래스의 멤버에 접근하기 위한 연산자.
// ::는 클래스 이름과 같이 쓰이지만, .는 클래스 객체와 함께 쓰인다.