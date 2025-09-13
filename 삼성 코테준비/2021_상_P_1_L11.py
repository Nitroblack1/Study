n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
move_info = [list(map(int, input().split())) for _ in range(m)]

directions = {
    1: [0, 1],
    2: [-1, 1],
    3: [-1, 0],
    4: [-1, -1],
    5: [0, -1],
    6: [1, -1],
    7: [1, 0],
    8: [1, 1]
}

def get_tree_sum():
    total = 0
    for i in range(n):
        for j in range(n):
            total += grid[i][j]
    return total


def inbound(i, j):
    if 0 <= i < n and 0 <= j < n:
        return True
    return False


def debug(board):
    for r in board:
        for c in r:
            print(int(c), end=" ")
        print()
    print()


vitamin = [
        [False for _ in range(n)]
        for _ in range(n)
    ]

vitamin[n-2][0], vitamin[n-1][0], vitamin[n-2][1], vitamin[n-1][1] = True, True, True, True

def simulate():
    y = 0
    while y < m:
        move(move_info[y])

        grow()

        buy()

        y += 1

    return get_tree_sum()


def move(m_info):
    global vitamin
    ds = directions.get(m_info[0])
    temp = [
        [False for _ in range(n)]
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            if vitamin[i][j]:
                ni, nj = get_index(i, j, ds[0], ds[1], m_info[1])
                temp[ni][nj] = True

    vitamin = [row[:] for row in temp]
    return


def get_index(ci, cj, di, dj, d):
    ni = (ci + di * d + n * d) % n
    nj = (cj + dj * d + n * d) % n
    return ni, nj


def grow():
    diagonal = [directions.get(i) for i in range(2, 9, 2)]

    for i in range(n):
        for j in range(n):
            if vitamin[i][j]:
                grid[i][j] += 1

    for i in range(n):
        for j in range(n):
            if vitamin[i][j]:
                for d in diagonal:
                    ni, nj = i + d[0], j + d[1]
                    if inbound(ni, nj) and grid[ni][nj] >= 1:
                        grid[i][j] += 1


def buy():
    global vitamin
    temp = [
        [False for _ in range(n)]
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 2 and not vitamin[i][j]:
                grid[i][j] -= 2
                temp[i][j] = True

    vitamin = [row[:] for row in temp]
############################################################
print(simulate())