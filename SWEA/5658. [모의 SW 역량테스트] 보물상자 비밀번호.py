import sys
#sys.stdin = open("input.txt", "r")

from collections import deque
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    nums = deque(input())

    line_length = n // 4    # 한 변의 길이
    candidates = set()

    for i in range(line_length):
        nums.appendleft(nums.pop())
        for j in range(4):    # 3 : 0~2, 3~5, 6~8, 9~11 # 4 : 0~3, 4~7, 8~11, 12~15
            hex_str = ''.join(list(nums)[j * line_length : (j + 1) * line_length])
            candidates.add(int(hex_str, 16))

    sorted_vals = sorted(candidates, reverse=True)
    answer = sorted_vals[k - 1]

    print(f"#{test_case} {answer}")