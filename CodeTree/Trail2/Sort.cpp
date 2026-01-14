#include <algorithm>    // To use 'sort' funciton
#include <functional>   // To use reverse Sort at 'sort' function
#include <iostream>

using namespace std;

int main() {
    int arr[8] = {12, 41, 37, 81, 19, 25, 60, 20};
    // sort(arr + 시작 인덱스, arr + 끝 인덱스 + 1); 형태
    sort(arr, arr + 8, greater<int>()); // 내림차순 정렬 -> need <functional> library
    sort(arr, arr + 8); // 오름차순 정렬
   
    for(int i = 0; i < 8; i++)   // 81, 60, 41, 37, 25, 20, 19, 12
        cout << arr[i] << " ";
    return 0;
}
