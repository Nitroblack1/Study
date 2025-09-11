n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
R, C, M1, M2, M3, M4, DIR = map(int, input().split())

# Please write your code here.

def rotate(r, c, m1, m2, m3, m4, dir):
    temp = grid[r-m1][c+m1]

    # CounterClockWise
    if dir == 0:
        # m1
        for i in range(0, m1):
            grid[r-m1+i][c+m1-i] = grid[r-m1+i+1][c+m1-i-1]
        # m4
        for i in range(0, m4):
            grid[r-i][c-i] = grid[r-i-1][c-i-1]
        # m3
        for i in range(0, m3):
            grid[r-m4-i][c-m4+i] = grid[r-m4-i-1][c-m4+i+1]
        # m2
        for i in range(0, m2):
            grid[r-m4-m3+i][c-m4+m3+i] = grid[r-m4-m3+i+1][c-m4+m3+i+1]

        grid[r-m1-1][c+m1-1] = temp

    # ClockWise
    if dir == 1:
        # m1 (↙ 방향으로 복사, 반시계 때의 m2 역할)
        for i in range(0, m1):
            grid[r - m1 + i][c + m1 - i] = grid[r - m1 + i - 1][c + m1 - i + 1]

        # m2 (↖ 방향, 반시계 때의 m3 역할)
        for i in range(0, m2):
            grid[r - m4 - m3 + i][c - m4 + m3 + i] = grid[r - m4 - m3 + i - 1][c - m4 + m3 + i - 1]

        # m3 (↗ 방향, 반시계 때의 m4 역할)
        for i in range(0, m3):
            grid[r - m4 - i][c - m4 + i] = grid[r - m4 - i + 1][c - m4 + i - 1]

        # m4 (↘ 방향, 반시계 때의 m1 역할)
        for i in range(0, m4):
            grid[r - i][c - i] = grid[r - i + 1][c - i + 1]

        # 마지막에 temp 삽입
        grid[r - m4 - m3 + 1][c - m4 + m3 - 1] = temp

rotate(R, C, M1, M2, M3, M4, DIR)
for row in grid:
    for element in row:
        print(element, end=" ")
    print()

