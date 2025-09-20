from collections import deque

r, c, k = map(int, input().split())
golem = [list(map(int, input().split())) for _ in range(k)]
forest = [
    [[0, False] for _ in range(c)]
    for _ in range(r + 3)
]


def debug(board):
    for i in board:
        for j in i:
            print(int(j), end=" ")
        print()


def ccw(d):
    if d == 0:
        return 3
    else:
        return d - 1


def cw(d):
    if d == 3:
        return 0
    else:
        return d + 1


def inb(i, j):
    if 3 <= i < r + 3 and 0 <= j < c:
        return True
    return False


def initialize_forest():
    global forest
    forest = [
        [[0, False] for _ in range(c)]
        for _ in range(r + 3)
    ]
    return


def is_entered(cen_idx):
    if cen_idx[0] >= 4 and 1 <= cen_idx[1] <= c - 2:
        return True
    return False


def drop(gol):
    ci, cj = 1, gol[0] - 1
    moved = True
    while moved:
        # 최남단까지 왔을 경우엔 브레이크
        if ci == r + 1:
            break

        moved, ci = move_south(ci, cj)
        if moved:
            continue
        moved, ci, cj, gol[1] = move_west(ci, cj, gol[1])
        if moved:
            continue
        moved, ci, cj, gol[1] = move_east(ci, cj, gol[1])
        if not moved:
            break

    return ci, cj, gol[1]


def move_south(ci, cj):
    # s_b check
    if ci + 2 < r + 3 and forest[ci + 2][cj][0] == 0:
        if forest[ci + 1][cj - 1][0] == 0:
            if forest[ci + 1][cj + 1][0] == 0:
                ci += 1
                return True, ci
    return False, ci


def move_west(ci, cj, ex):
    # w_b check
    if cj - 2 >= 0 and forest[ci][cj - 2][0] == 0:
        if forest[ci - 1][cj - 1][0] == 0:
            if forest[ci + 1][cj - 1][0] == 0:
                if forest[ci + 1][cj - 2][0] == 0:
                    if forest[ci + 2][cj - 1][0] == 0:
                        ci, cj = ci + 1, cj - 1
                        ex = ccw(ex)
                        return True, ci, cj, ex
    return False, ci, cj, ex


def move_east(ci, cj, ex):
    # e_b check
    if cj + 2 < c and forest[ci][cj + 2][0] == 0:
        if forest[ci - 1][cj + 1][0] == 0:
            if forest[ci + 1][cj + 1][0] == 0:
                if forest[ci + 2][cj + 1][0] == 0:
                    if forest[ci + 1][cj + 2][0] == 0:
                        ci, cj = ci + 1, cj + 1
                        ex = cw(ex)
                        return True, ci, cj, ex
    return False, ci, cj, ex

dss = [-1, 0], [0, 1], [1, 0], [0, -1]
def draw(ci, cj, gol_num, ex):
    forest[ci][cj][0] = gol_num
    for i in range(4):
        if i == ex:
            forest[ci + dss[i][0]][cj + dss[i][1]] = [gol_num, True]
        else:
            forest[ci + dss[i][0]][cj + dss[i][1]][0] = gol_num


def nymph(cen, c_gol):
    max_row = cen[0]
    avail_gol = [c_gol]
    visited = [
        [False for _ in range(c)]
        for _ in range(r + 3)
    ]
    q = deque()
    q.append((cen[0], cen[1]))
    visited[cen[0]][cen[1]] = True

    while q:
        ci, cj = q.popleft()
        # 만약 출구라면
        if forest[ci][cj][1]:
            for ds in dss:
                ni, nj = ci + ds[0], cj + ds[1]
                if inb(ni, nj) and not visited[ni][nj]:
                    if forest[ni][nj][0] != 0:
                        q.append((ni, nj))
                        visited[ni][nj] = True
                        max_row = max(max_row, ni)
                        avail_gol.append(forest[ni][nj][0])
        else:
            for ds in dss:
                ni, nj = ci + ds[0], cj + ds[1]
                if inb(ni, nj) and not visited[ni][nj]:
                    for gol in avail_gol:
                        if forest[ni][nj][0] == gol:
                            q.append((ni, nj))
                            visited[ni][nj] = True
                            max_row = max(max_row, ni)

    return max_row - 2


def explore():
    num = 0
    total_row = 0
    while num < k:
        cen_i, cen_j, ex = drop(golem[num])
        if not is_entered([cen_i, cen_j]):
            initialize_forest()
            num += 1
            continue
        draw(cen_i, cen_j, num + 1, ex)
        total_row += nymph([cen_i, cen_j], num + 1)
        num += 1

    return total_row


####################################################
print(explore())