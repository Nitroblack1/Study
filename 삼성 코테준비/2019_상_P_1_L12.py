MAX_N = 100
MAX_NUM = 100

# 변수 선언 및 입력
n, m = 3, 3
r, c, k = tuple(map(int, input().split()))

grid = [
    [0 for _ in range(2 * MAX_N + 1)]
    for _ in range(2 * MAX_N + 1)
]


# row 행에 대해 숫자 놀이를 진행합니다.
def row_play(row):
    # 각 숫자에 대해 빈도수를 구해줍니다.
    # 정렬시 빈도수, 숫자 순으로 오름차순 정렬이 되도록
    # (빈도수, 숫자) 형태로 저장해줍니다.
    pairs = list()
    for num in range(1, MAX_NUM + 1):
        frequency = sum([1 for col in range(1, m + 1) if grid[row][col] == num])

        if frequency:
            pairs.append((frequency, num))

    # 숫자를 새로 적어줘야 하므로,
    # 그 전에 기존 row 행에 있던 숫자들을 전부 0으로 바꿔줍니다.
    for col in range(1, m + 1):
        grid[row][col] = 0

    pairs.sort()

    # row 행에 새로운 숫자를 차례대로 적어줍니다.
    for i, (frequency, num) in enumerate(pairs):
        grid[row][i * 2 + 1] = num
        grid[row][i * 2 + 2] = frequency

    return len(pairs) * 2


# col 열에 대해 숫자 놀이를 진행합니다.
def col_play(col):
    # 각 숫자에 대해 빈도수를 구해줍니다.
    # 정렬시 빈도수, 숫자 순으로 오름차순 정렬이 되도록
    # (빈도수, 숫자) 형태로 저장해줍니다.
    pairs = list()
    for num in range(1, MAX_NUM + 1):
        frequency = sum([
            1
            for row in range(1, n + 1)
            if grid[row][col] == num
        ])

        if frequency:
            pairs.append((frequency, num))

    # 숫자를 새로 적어줘야 하므로,
    # 그 전에 기존 col 열에 있던 숫자들을 전부 0으로 바꿔줍니다.
    for row in range(1, n + 1):
        grid[row][col] = 0

    pairs.sort()

    # col 열에 새로운 숫자를 차례대로 적어줍니다.
    for i, (frequency, num) in enumerate(pairs):
        grid[i * 2 + 1][col] = num
        grid[i * 2 + 2][col] = frequency

    return len(pairs) * 2


def simulate():
    global n, m
    # 행의 개수가 열의 개수와 일치하거나 더 많다면
    # 행 단위로 진행 후, 최대로 긴 열의 크기를 구합니다.
    if n >= m:
        m = max([
            row_play(row) for row in range(1, n + 1)
        ])
    # 열의 개수가 더 많다면
    # 열 단위로 진행 후, 최대로 긴 행의 크기를 구합니다.
    else:
        n = max([
            col_play(col) for col in range(1, m + 1)
        ])


for i in range(1, n + 1):
    given_row = list(map(int, input().split()))
    for j, elem in enumerate(given_row, start=1):
        grid[i][j] = elem

ans = -1
# 최대 100초 동안 시뮬레이션을 진행합니다.
for t in range(0, 100):
    if grid[r][c] == k:
        ans = t
        break

    simulate()

print(ans)
