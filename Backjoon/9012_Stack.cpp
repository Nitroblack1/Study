#include <iostream>
#include <string>

#define MAX_N 50

int top;
int stack[MAX_N];

void stackInit() {
    top = 0;
}

bool stackIsFull() {
    return (top == MAX_N);
}

bool stackIsEmpty() {
    return (top == 0);
}

int stackPush(char value) {
    if (stackIsFull()) {
        return 0;
    }

    stack[top++] = value;
    return 1;
}

int stackPop() {
    if (stackIsEmpty()) {
        return 0;
    }

    top--;
    return 1;
}

int main() {
    int n;
    std::cin >> n;

    while (n--) {
        std::string str;
        std::cin >> str;

        int balance = 0;
        bool valid = true;

        for (char c : str) {
            if (c == '(') {
                balance++;
            } else {
                if (balance == 0) {
                    valid = false;
                    break;
                }
                balance--;
            }
        }
        if (valid && balance == 0) std::cout << "YES\n";
        else std::cout << "NO\n";
    }    
}