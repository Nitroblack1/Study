#include <iostream>
#include <deque>
#include <string>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int Q;
    cin >> Q;
    string line;
    getline(cin, line);

    deque<char> dq; // back -> front (push at back = push_front, pop at front = pop_back)
    long long ballCnt = 0, wallCnt = 0;

    // direction of the "front" end: 0=RIGHT(initial), 1=DOWN, 2=LEFT, 3=UP
    int dir = 0;

    auto applyGravity = [&]()
    {
        // Vertical only
        if (dir == 1)
        { // front end is DOWN => bottom is front end => dq.back()
            while (!dq.empty() && dq.back() == 'b')
            {
                dq.pop_back();
                --ballCnt;
            }
        }
        else if (dir == 3)
        { // front end is UP => bottom is back end => dq.front()
            while (!dq.empty() && dq.front() == 'b')
            {
                dq.pop_front();
                --ballCnt;
            }
        }
    };

    for (int i = 0; i < Q; ++i)
    {
        getline(cin, line);

        if (line == "pop")
        {
            if (!dq.empty())
            {
                char x = dq.back(); // pop from front end
                dq.pop_back();
                if (x == 'b')
                    --ballCnt;
                else
                    --wallCnt;
                applyGravity();
            }
        }
        else if (line.rfind("push ", 0) == 0)
        {
            char x = line[5]; // 'b' or 'w'
            dq.push_front(x); // push at back end
            if (x == 'b')
                ++ballCnt;
            else
                ++wallCnt;
            applyGravity();
        }
        else if (line.rfind("rotate ", 0) == 0)
        {
            char d = line[7]; // 'l' or 'r'
            if (d == 'r')
                dir = (dir + 1) % 4; // clockwise
            else
                dir = (dir + 3) % 4; // counter-clockwise
            applyGravity();
        }
        else if (line == "count b")
        {
            cout << ballCnt << "\n";
        }
        else if (line == "count w")
        {
            cout << wallCnt << "\n";
        }
    }

    return 0;
}