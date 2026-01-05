#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    //////////////////////////////////////////////////////////////////////////////
    // ENUMERATION EXAMPLES
    enum MonthLength {
        JANUARY = 31,
        FEBRUARY = 28,
        MARCH = 31,
        APRIL = 30,
        MAY = 31,
        JUNE = 30,
        JULY = 31,
        AUGUST = 31,
        SEPTEMBER = 30,
        OCTOBER = 31,
        NOVEMBER = 30,
        DECEMBER = 31
    };

    enum Direction {
        NORTH,      // 0
        EAST,       // 1
        SOUTH = -3, // -3
        WEST        // -2
    };
    
    //////////////////////////////////////////////////////////////////////////////
    // COMMA OPERATOR, CONTINUE, BREAK EXAMPLES
    int first, second, third;
    int result = ((first = 2, second = first + 1), third = second + 1);
    std::cout << "Result of comma operator: " << result << "\n";

    // continue : skip current iteration, break : exit loop
    // if loop is nested, those two only affect the innermost loop

    //////////////////////////////////////////////////////////////////////////////
    // FILE STREAM EXAMPLES
    // [player.txt]
    // 100
    // John Doe
    ifstream inputStream;
    inputStream.open("player.txt");

    string firstName, lastName, text;
    int score;
    inputStream >> score;
    inputStream >> firstName >> lastName;

    while (inputStream >> text)     // false when readable stream ends
    {
        cout << text << endl;
    }

    return 0;
}