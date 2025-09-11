from collections import deque

n, q = map(int, input().split())
n = pow(2, n)
grid = [list(map(int, input().split())) for _ in range(n)]
rot_lv = list(map(int, input().split()))

dis, djs = [0, 1, 0, -1], [1, 0, -1, 0]

def debug(tgt):
    for r in tgt:
        for c in r:
            print(c, end=" ")
        print()
    print()


def inbound(i, j):
    if 0 <= i < n and 0 <= j < n:
        return True
    return False


def rotate(turn):
    # 1, 2 -> s:2, u:1 / s:4, u:2
    size = pow(2, rot_lv[turn])
    unit = pow(2, rot_lv[turn] - 1)

    if size == 1:
        return

    for row in range(n//size):
        for col in range(n//size):
            start_pos = [row * size, col * size]
            do_rotate(start_pos, size, unit)

    return


def do_rotate(start_pos, size, unit):
    # start_pos는 격자 단위 시작점 : [0, 0], [0, 4], ...
    # unit은 격자 내부 회전 단위 : 4 / 2 / 1
    # size는 격자 사이즈 : 8 / 4 / 2
    sub = [
        row[start_pos[1]:start_pos[1] + size]
        for row in grid[start_pos[0]:start_pos[0] + size]
    ]
    sub_rot = [
        [0 for _ in range(size)]
        for _ in range(size)
    ]

    for i in range(2):
        for j in range(2):
            sub_block = [r[j*unit : (j+1)*unit] for r in sub[i*unit : (i + 1)*unit]]
            sub_st_p = [j * unit, (1 - i) * unit]
            for ui in range(unit):
                for uj in range(unit):
                    sub_rot[sub_st_p[0] + ui][sub_st_p[1] + uj] = sub_block[ui][uj]

    for i in range(size):
        for j in range(size):
            grid[start_pos[0] + i][start_pos[1] + j] = sub_rot[i][j]

    return


def melt():
    global grid
    temp_grid = [row[:] for row in grid]

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                continue
            near_count = 0
            for di, dj in zip(dis, djs):
                ni, nj = i + di, j + dj
                if inbound(ni, nj) and grid[ni][nj] > 0:
                    near_count += 1
            if near_count < 3:
                temp_grid[i][j] -= 1

    grid = [row[:] for row in temp_grid]
    return


def get_max_area_and_total_ice():
    max_area = 0
    total_ice = 0
    visited = [
        [False for _ in range(n)]
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            total_ice += grid[i][j]
            if not visited[i][j] and grid[i][j] > 0:
                # 같은 visited로 작업해야 한다.
                max_area = max(max_area, bfs(i, j, visited))

    return total_ice, max_area


def bfs(i, j, visited):
    bfs_q = deque()
    area = 1

    visited[i][j] = True
    bfs_q.append((i, j))
    while bfs_q:
        ci, cj = bfs_q.popleft()
        for di, dj in zip(dis, djs):
            ni, nj = ci + di, cj + dj
            if inbound(ni, nj):
                if not visited[ni][nj] and grid[ni][nj] > 0:
                    area += 1
                    visited[ni][nj] = True
                    bfs_q.append((ni, nj))

    return area


def simulate():
    turn = 0
    while turn < q:
        rotate(turn)
        melt()
        turn += 1
    total_ice, max_area = get_max_area_and_total_ice()

    print(total_ice)
    print(max_area)


################################################################
############################# Main #############################
simulate()