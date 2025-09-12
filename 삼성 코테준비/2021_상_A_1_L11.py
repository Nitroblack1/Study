n = int(input())
list_size = pow(n, 2)
prefer_list = [list(map(int, input().split())) for _ in range(list_size)]
grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 좌, 하, 우, 상
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


def simulate():
    idx = 0
    while idx < len(prefer_list):
        cur_p = prefer_list[idx]

        # 1. prefer
        is_located, areas = prefer_num(cur_p)
        if is_located:
            allocate(cur_p[0], areas)
            idx += 1
            continue

        # 2. empty
        is_located, areas = empty_num(areas)
        if is_located:
            allocate(cur_p[0], areas)
            idx += 1
            continue

        # 3. row, col min
        allocate(cur_p[0], row_col_min(areas))
        idx += 1


def allocate(p, area):
    i, j = area[0][0], area[0][1]
    grid[i][j] = p
    return


def prefer_num(p_info):
    target = []
    prefer = [p_info[1], p_info[2], p_info[3], p_info[4]]
    max_num = 0
    temp_grid = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                continue
            for di, dj in zip(dis, djs):
                ni, nj = i + di, j + dj
                if inbound(ni, nj):
                    for pref in prefer:
                        if grid[ni][nj] == pref:
                            temp_grid[i][j] += 1

            if max_num < temp_grid[i][j]:
                target = [[i, j]]
                max_num = temp_grid[i][j]
            elif max_num == temp_grid[i][j]:
                target.append([i, j])

    if len(target) == 1:
        return True, target
    else:
        return False, target


def empty_num(areas):
    target = []
    temp_grid = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    max_num = 0

    for area in areas:
        for di, dj in zip(dis,djs):
            ni, nj = area[0] + di, area[1] + dj
            if inbound(ni, nj):
                if grid[ni][nj] == 0:
                    temp_grid[area[0]][area[1]] += 1

        if max_num < temp_grid[area[0]][area[1]]:
            target = [[area[0], area[1]]]
            max_num = temp_grid[area[0]][area[1]]
        elif max_num == temp_grid[area[0]][area[1]]:
            target.append([area[0], area[1]])

    if len(target) == 1:
        return True, target
    else:
        return False, target


def row_col_min(areas):
    areas.sort(key=lambda x: [x[0], x[1]])
    return [areas[0]]


def get_score():
    score = 0

    for i in range(n):
        for j in range(n):
            cur_p = grid[i][j]
            count = 0
            for prefer in prefer_list:
                if prefer[0] == cur_p:
                    for di, dj in zip(dis, djs):
                        ni, nj = i + di, j + dj
                        if inbound(ni, nj):
                            for pref in prefer[1:]:
                                if pref == grid[ni][nj]:
                                    count += 1
                    score += int(pow(10, count - 1))
                    break

    return score


#############################################################
simulate()
print(get_score())