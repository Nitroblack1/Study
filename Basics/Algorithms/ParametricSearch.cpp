/*
Parametric Search란,
정답 후보 값을 이분 탐색하면서, 각 후보가 조건을 만족하는지 판정하는 방식으로 최적의 값을 찾는 알고리즘 기법이다.

[문제]
길이가 각각 다른 K개의 리본을 가지고 있다.
공예작품을 만들기 위해 가지고 있는 리본을 잘라서 길이가 동일한 N개의 리본재료를 만들려고 한다.
리본재료의 최대 길이를 구하시오. ( 1 <= K <= 10,000; 1 <= N <= 1,000,000; K <= N )
- 손실되는 길이는 없음
- 만들 수 없는 경우는 없다
- 이미 자른 리본은 붙일 수 없다
- 자를 때는 정수 cm 단위로 자른다

[접근법]
답을 찍어본다. -> 그 답이 되냐 안 되냐를 확인한다. -> 되면 줄이고, 안 되면 늘린다.
*/

#include <iostream>

using namespace std;

#define MAX_RIBBON 100

int K, N;       // K : 리본의 개수, N : 필요한 리본재료의 개수
int lowV, highV, midV;  // lowV : 리본재료 길이의 최솟값, highV : 리본재료 길이의 최댓값, midV : 리본재료 길이의 중간값
int numRibbonTape, bestV;   // numRibbonTape : midV 길이로 잘랐을 때 얻어지는 리본재료의 개수, bestV : 리본재료 길이의 최적값
int sizeRibbonTape[MAX_RIBBON];   // sizeRibbonTape[] : 리본의 길이 배열

void search() {
    midV = lowV + (highV - lowV) / 2;   // 중간값 계산
    numRibbonTape = 0;

    for (int i = 0; i < K; i++) {   // 리본 자르기
        numRibbonTape += sizeRibbonTape[i] / midV;
    }

    if (numRibbonTape >= N) {   // 리본재료를 N개 이상 만들 수 있는 경우
        if (bestV < midV) {
            bestV = midV;   // 최적값 갱신
            lowV = midV + 1;    // 길이를 늘려본다
        } else {    // N개를 만들지 못한 경우 -> 길이를 줄여야 한다
            highV = midV - 1;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;

    for (int test_case = 1; test_case <= T; test_case++) {
        lowV = 1;
        highV = 0;
        bestV = -1;

        cin >> K >> N;

        for (int i = 0; i < K; i++) {
            cin >> sizeRibbonTape[i];
            if (highV < sizeRibbonTape[i]) {
                highV = sizeRibbonTape[i];   // 리본재료 길이의 최댓값 갱신
            }
        }

        while (lowV <= highV) {
            search();
        }

        cout << "#" << test_case << " " << bestV << "\n";
    }

    return 0;
}