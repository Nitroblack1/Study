from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

STONE, RED, EMPTY = -1, 0, -2

def debug(board):
    for r in board:
        for c in r:
            print(c, end=" ")
        print()
    print()


def bomb_exist():
    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 0:
                return True
    return False


def simulate():
    score = 0
    while bomb_exist():

        area = find_max_area()
        if len(area) >= 2:
            bomb(area)
            score += pow(len(area), 2)
        else:
            break

        gravity()

        rotate()

        gravity()

    return score


# find max area > min red > max row > min col
def find_max_area():
    areas = []

    for i in range(n):
        for j in range(n):
            # RED, STONE 제외
            if grid[i][j] <= 0:
                continue
            areas.append(list(get_area_bfs(i, j)))

    # max_area
    areas.sort(key=lambda x: [[-x[1], x[2], -x[0][0], x[0][1]]])

    return areas[0][3]


def inbound(i, j):
    if 0 <= i < n and 0 <= j < n:
        return True
    return False


def get_area_bfs(i, j):
    dis, djs = [0, 1, 0, -1], [1, 0, -1, 0]
    q = deque()
    visited = [
        [False for _ in range(n)]
        for _ in range(n)
    ]

    area = [[i, j]]
    red_area = []
    cur_color = grid[i][j]
    size = 1
    red_count = 0

    visited[i][j] = True
    q.append((i, j))
    while q:
        ci, cj = q.popleft()
        for di, dj in zip(dis, djs):
            ni, nj = ci + di, cj + dj
            if inbound(ni, nj) and not visited[ni][nj]:
                # 같은 색이거나 red bomb면 군집 포함.
                if grid[ni][nj] == cur_color or grid[ni][nj] == RED:
                    q.append((ni, nj))
                    visited[ni][nj] = True
                    size += 1
                    # red는 area에 명시적으로 추가하진 않음 for sort
                    if grid[ni][nj] == RED:
                        red_count += 1
                        red_area.append([ni, nj])
                    else:
                        area.append([ni, nj])

    area.sort(key=lambda x: [-x[0], x[1]])
    return area[0], size, red_count, area + red_area


def bomb(area):
    for elem in area:
        grid[elem[0]][elem[1]] = EMPTY


def gravity():
    for col in range(n):
        idx = n - 1
        temp_col = [-2 for _ in range(n)]
        for row in range(n-1, -1, -1):
            if grid[row][col] == STONE:
                temp_col[row] = grid[row][col]
                idx = row - 1
                continue
            if grid[row][col] == EMPTY:
                continue
            else:
                temp_col[idx] = grid[row][col]
                idx -= 1

        for row in range(n):
            grid[row][col] = temp_col[row]


def rotate():
    global grid
    rot = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            rot[n - j - 1][i] = grid[i][j]

    grid = [row[:] for row in rot]
    return


##########################################################
print(simulate())