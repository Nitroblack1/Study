#include <string>
#include <iostream>
#define MAX_N 10000

int top;
int stack[MAX_N];

void stackInit() { top = 0; }
bool empty() { return (top == 0); }
bool full() { return (top == MAX_N); }

void push(int x) {
    if (!full()) {
        stack[top++] = x;
    }
}

int pop() {
    if (empty()) {
        return -1;
    }

    return stack[--top];
}

int size() { return top; }

int getTop() { return empty() ? -1 : stack[top - 1]; }

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int T;
    std::cin >> T;
    std::cin.ignore();

    while (T--) {
        std::string line, cmd;
        std::cin >> cmd;

        if (cmd == "push") {
            int x;
            std::cin >> x;
            push(x);
        }
        else if (cmd == "pop") {
            int value;
            std::cout << pop() << "\n";
        }
        else if (cmd == "size") {
            std::cout << size() << "\n";
        }
        else if (cmd == "empty") {
            std::cout << int(empty()) << "\n";
        }
        else if (cmd == "top") {
            std::cout << getTop() << "\n";
        }
    }
    return 0;
}