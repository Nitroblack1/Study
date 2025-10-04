#import sys
#sys.stdin = open("input.txt", "r")

RU, LU, RD, LD = [-1, 1], [-1, -1], [1, 1], [1, -1]

def inb(r, c):
    return 0 <= r < n and 0 <= c < n


def inb_corners(i, j, rr, ll):
    if not inb(i - ll, j - ll) or not inb(i - rr - ll, j + rr - ll):
        return False
    return True


def travel(i, j, rr, ll):
    cafe_list = set()

    std = 0
    while std < rr:
        length = len(cafe_list)
        cafe_list.add(grid[i + RU[0] * std][j + RU[1] * std])
        if length == len(cafe_list):
            return - 1
        std += 1

    std = 0
    while std < ll:
        length = len(cafe_list)
        cafe_list.add(grid[i - rr + LU[0] * std][j + rr + LU[1] * std])
        if length == len(cafe_list):
            return -1
        std += 1

    std = 0
    while std < rr:
        length = len(cafe_list)
        cafe_list.add(grid[i - rr - ll + LD[0] * std][j + rr - ll + LD[1] * std])
        if length == len(cafe_list):
            return -1
        std += 1

    std = 0
    while std < ll:
        length = len(cafe_list)
        cafe_list.add(grid[i - ll + RD[0] * std][j - ll + RD[1] * std])
        if length == len(cafe_list):
            return -1
        std += 1

    return len(cafe_list)



T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    ans = -1
    for i in range(2, n):
        for j in range(1, n-1):
            for rr in range(1, n-1):
                if not inb(i - rr, j + rr):
                    break
                for ll in range(1, n-1):
                    if not inb_corners(i, j, rr, ll):
                        break
                    ans = max(ans, travel(i, j, rr, ll))


    print(f'#{test_case} {ans}')