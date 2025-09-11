k = int(input())

blocks_info = []
for _ in range(k):
    blocks_info.append(list(map(int, input().split())))

# Block types. start index is 0, 0 fixed
b1 = [[0, 0]]
b2 = [
    [0, 0],
    [0, 1]
]
b3 = [
    [0, 0],
    [1, 0]
]
block_type = [[], b1, b2, b3]

# check each area filled as T/F
# red_area : 0 <= i <= 3, 6 <= j <= 9
# pink_area : 0 <= i <= 3,  4 <= j <= 5

# lemon_area : 4 <= i <= 5, 0 <= j <= 3
# yellow_area : 6 <= i <= 9, 0 <= j <= 3
tetris_area = [[False] * 10 for _ in range(10)]

def tetris():
    global score
    # block_info[0] : type / [1] : i / [2] : j
    for block_info in blocks_info:
        # ex) b2(--) -> [[1, 2], [1, 3]]
        cur_block_area = []
        si, sj = block_info[1], block_info[2]
        # get block_area before drop (is on blue area)
        for area in block_type[block_info[0]]:
            cur_block_area.append([si + area[0], sj + area[1]])

        # print(cur_block_area)

        red_drop(cur_block_area)
        yellow_drop(cur_block_area)
        check_pop()
        check_soft_area()

        #### debug ####
        # print('red')
        # for r in range(4):
        #     for c in range(4, 10):
        #         print(tetris_area[r][c], end=" ")
        #     print()
        # print()
        #
        # print('yellow')
        # for r in range(4, 10):
        #     for c in range(4):
        #         print(tetris_area[r][c], end=" ")
        #     print()
        # print()
        #### debug ####

    return


def red_drop(b_poses):
    dj = 1
    if len(b_poses) == 2:
        p1, p2 = b_poses[0], b_poses[1]
        # 바깥으로 벗어나지 않고, 다른 블록과 겹치지 않을 때까지 오른쪽으로 이동
        while p1[1] + dj < 10 and p2[1] + dj < 10 and not tetris_area[p1[0]][p1[1] + dj] and not tetris_area[p2[0]][p2[1] + dj]:
            dj += 1
        tetris_area[b_poses[0][0]][b_poses[0][1] + dj - 1] = True
        tetris_area[b_poses[1][0]][b_poses[1][1] + dj - 1] = True

    if len(b_poses) == 1:
        p = b_poses[0]
        while p[1] + dj < 10 and not tetris_area[p[0]][p[1] + dj]:
            dj += 1
        tetris_area[b_poses[0][0]][b_poses[0][1] + dj - 1] = True

def yellow_drop(b_poses):
    di = 1
    if len(b_poses) == 2:
        p1, p2 = b_poses[0], b_poses[1]
        # 바깥으로 벗어나지 않고, 다른 블록과 겹치지 않을 때까지 오른쪽으로 이동
        while p1[0] + di < 10 and p2[0] + di < 10 and not tetris_area[p1[0] + di][p1[1]] and not tetris_area[p2[0] + di][
            p2[1]]:
            di += 1
        tetris_area[b_poses[0][0] + di - 1][b_poses[0][1]] = True
        tetris_area[b_poses[1][0] + di - 1][b_poses[1][1]] = True

    if len(b_poses) == 1:
        p = b_poses[0]
        while p[0] + di < 10 and not tetris_area[p[0] + di][p[1]]:
            di += 1
        tetris_area[b_poses[0][0] + di - 1][b_poses[0][1]] = True
    return


def check_pop():
    global score
    # for red
    for c in range(6, 10):
        is_filled = True
        for r in range(4):
            # if col is not filled
            if not tetris_area[r][c]:
                is_filled = False
                break
        if is_filled:
            # else, pop and add score!
            score += 1
            q = 0
            while c - q >= 6:
                for row in range(4):
                    # 해당 열을 오른쪽으로 밀어주고
                    tetris_area[row][c - q] = tetris_area[row][c - q - 1]
                    # 혹시 모르니 이동했던 열은 전부 False로 바꾼다.
                    tetris_area[row][c - q - 1] = False
                q += 1

    # for yellow
    for r in range(6, 10):
        is_filled = True
        for c in range(4):
            # row is not filled
            if not tetris_area[r][c]:
                is_filled = False
                break
        if is_filled:
            # else, pop and add score!
            score += 1
            q = 0
            while r - q >= 6:
                for col in range(4):
                    tetris_area[r - q][col] = tetris_area[r - q - 1][col]
                    tetris_area[r - q - 1][col] = False
                q += 1


def check_soft_area():
    # for red
    for c in range(4, 6):
        for r in range(4):
            if tetris_area[r][c]:
                push = 0
                while 6 - c - push > 0:
                    for col in range(9, c, -1):
                        for row in range(4):
                            tetris_area[row][col] = tetris_area[row][col - 1]
                            # 혹시 모르니 이동했던 열은 전부 False로 바꾼다.
                            tetris_area[row][col - 1] = False
                    push += 1

    # for yellow
    for r in range(4, 6):
        for c in range(4):
            if tetris_area[r][c]:
                push = 0
                while 6 - r - push > 0:
                    for row in range(9, r, -1):
                        for col in range(4):
                            tetris_area[row][col] = tetris_area[row - 1][col]
                            tetris_area[row - 1][col] = False
                    push += 1

    return


def get_filled_area():
    global total_area
    # red_area
    for r in range(4):
        for c in range(6, 10):
            if tetris_area[r][c]:
                total_area += 1

    # yellow_area
    for r in range(6, 10):
        for c in range(4):
            if tetris_area[r][c]:
                total_area += 1

##################### Main #####################
score = 0
total_area = 0
tetris()
get_filled_area()
print(score)
print(total_area)