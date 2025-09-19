from collections import deque

k, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(5)]
piece_num = list(map(int, input().split()))
dis, djs = [0, 1, 0, -1], [1, 0, -1, 0]

def debug(board):
    for r in board:
        for c in r:
            print(c, end=" ")
        print()
    print()


def inb(r, c):
    if 0 <= r < 5 and 0 <= c < 5:
        return True
    return False


def rotate_90(c):
    temp = [row[c[1]-1:c[1]+2] for row in grid[c[0]-1:c[0]+2]]
    temp_rot = [
        [0 for _ in range(3)]
        for _ in range(3)
    ]
    temp_grid = [row[:] for row in grid]

    for i in range(3):
        for j in range(3):
            temp_rot[j][3 - i - 1] = temp[i][j]

    for i in range(3):
        for j in range(3):
            temp_grid[c[0] - 1 + i][c[1] - 1 + j] = temp_rot[i][j]

    return temp_grid


def rotate_180(c):
    temp = [row[c[1] - 1:c[1] + 2] for row in grid[c[0] - 1:c[0] + 2]]
    temp_rot = [
        [0 for _ in range(3)]
        for _ in range(3)
    ]
    temp_grid = [row[:] for row in grid]

    for i in range(3):
        for j in range(3):
            temp_rot[3 - i - 1][3 - j - 1] = temp[i][j]

    for i in range(3):
        for j in range(3):
            temp_grid[c[0] - 1 + i][c[1] - 1 + j] = temp_rot[i][j]

    return temp_grid


def rotate_270(c):
    temp = [row[c[1] - 1:c[1] + 2] for row in grid[c[0] - 1:c[0] + 2]]
    temp_rot = [
        [0 for _ in range(3)]
        for _ in range(3)
    ]
    temp_grid = [row[:] for row in grid]

    for i in range(3):
        for j in range(3):
            temp_rot[3 - j - 1][i] = temp[i][j]

    for i in range(3):
        for j in range(3):
            temp_grid[c[0] - 1 + i][c[1] - 1 + j] = temp_rot[i][j]

    return temp_grid


def explore():
    max_t = 0
    max_b = []
    max_std = (3, 100, 100)
    for i in range(1, 4):
        for j in range(1, 4):
            # print(i, j)

            cur_t, b = calculate(rotate_90([i, j]))
            # print('90', cur_t)
            # debug(b)
            if max_t < cur_t:
                max_std = (0, j, i)
                max_t = cur_t
                max_b = b
            if max_t == cur_t:
                if max_std > (0, j, i):
                    max_std = (0, j, i)
                    max_t = cur_t
                    max_b = b


            cur_t, b = calculate(rotate_180([i, j]))
            # print('180', cur_t)
            # debug(b)
            if max_t < cur_t:
                max_std = (1, j, i)
                max_t = cur_t
                max_b = b
            if max_t == cur_t:
                if max_std > (1, j, i):
                    max_std = (1, j, i)
                    max_t = cur_t
                    max_b = b

            cur_t, b = calculate(rotate_270([i, j]))
            # print('270', cur_t)
            # debug(b)
            if max_t < cur_t:
                max_std = (2, j, i)
                max_t = cur_t
                max_b = b
            if max_t == cur_t:
                if max_std > (2, j, i):
                    max_std = (2, j, i)
                    max_t = cur_t
                    max_b = b







    return max_t, max_b

# 해당 맵에서 유물 갯수
def calculate(board):
    treasure = 0
    visited = [
        [False for _ in range(5)]
        for _ in range(5)
    ]

    for i in range(5):
        for j in range(5):
            if not visited[i][j] and board[i][j] != 0:
                visited[i][j] = True
                t = find_max_bfs([i, j], board, visited)
                if t >= 3:
                    treasure += t

    return treasure, board


def find_max_bfs(s, board, visited):
    std = board[s[0]][s[1]]

    q = deque()
    q.append((s[0], s[1]))
    visited[s[0]][s[1]] = True

    count = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in zip(dis, djs):
            ni, nj = ci + di, cj + dj
            if inb(ni, nj) and not visited[ni][nj]:
                if board[ni][nj] == std:
                    count += 1
                    q.append((ni, nj))
                    visited[ni][nj] = True

    return count


def pop():
    flag = False
    for i in range(5):
        for j in range(5):
            if grid[i][j] != 0:
                is_popped = pop_bfs([i, j])
                if is_popped:
                    flag = True

    return flag


def pop_bfs(s):
    q = deque()
    visited = [
        [False for _ in range(5)]
        for _ in range(5)
    ]
    std = grid[s[0]][s[1]]
    count = 1
    pop_area = [[s[0], s[1]]]

    visited[s[0]][s[1]] = True
    q.append((s[0], s[1]))
    while q:
        ci, cj = q.popleft()
        for di, dj in zip(dis, djs):
            ni, nj = ci + di, cj + dj
            if inb(ni, nj) and not visited[ni][nj]:
                if grid[ni][nj] == std:
                    visited[ni][nj] = True
                    count += 1
                    q.append((ni, nj))
                    pop_area.append([ni, nj])

    if count >= 3:
        for area in pop_area:
            grid[area[0]][area[1]] = 0
        return True

    return False


def fill():
    global fill_idx
    for col in range(5):
        for row in range(4, -1, -1):
            if grid[row][col] == 0 and fill_idx < m:
                grid[row][col] = piece_num[fill_idx]
                fill_idx += 1
    return


##############################################
turn = 0
fill_idx = 0
while turn < k:
    cur_fill_idx = fill_idx

    max_treasure, grid = explore()

    if max_treasure < 3:
        break

    is_chain = pop()
    while is_chain:
        fill()

        is_chain = pop()
        if not is_chain:
            break

    print(fill_idx - cur_fill_idx, end=" ")
    turn += 1