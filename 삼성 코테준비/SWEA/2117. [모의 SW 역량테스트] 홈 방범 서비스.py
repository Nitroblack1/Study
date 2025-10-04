import sys
sys.stdin = open("input.txt", "r")


def simulate():
    max_h = 0
    for i in range(n):
        for j in range(n):
            for k in range(1, int(1.5 * n) + 1):
                cost = k*k + (k-1)*(k-1)
                cur_h = 0
                for r in range(n):
                    for c in range(n):
                        if abs(r - i) + abs(c - j) < k and grid[r][c] == 1:
                            cur_h += 1

                if cur_h * m >= cost:
                    max_h = max(max_h, cur_h)

    return max_h


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    indices = set()
    ans = simulate()

    print(f'#{test_case} {ans}')