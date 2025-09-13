n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
attacks = [list(map(int, input().split())) for _ in range(m)]

directions = {
    0 : [0, 1],
    1 : [1, 0],
    2 : [0, -1],
    3 : [-1, 0]
}

player = [n//2, n//2]


def debug(board):
    for r in board:
        for c in r:
            print(c, end=" ")
        print()
    print()


def game():
    turn = 0
    while turn < m:
        attack(attacks[turn])

        monsters = fill()

        removed = True
        # remove에서는 삭제만
        while removed:
            removed, monsters = remove(monsters)

        fill_map(monsters)

        monsters = generate(monsters)

        fill_map(monsters)

        turn += 1

    return


def attack(at_info):
    global score
    ds = directions.get(at_info[0])
    at_range = at_info[1]

    l = 1
    while l <= at_range:
        score += grid[player[0] + ds[0]*l][player[1] + ds[1]*l]
        grid[player[0] + ds[0]*l][player[1] + ds[1]*l] = 0
        l += 1

    return

# 빈 칸 제거된 리스트를 가져와서 맵에 채워넣고, 몬스터 리스트 리턴
def fill():
    monsters = get_list()
    fill_map(monsters)
    return monsters


def get_list():
    ds1 = [[0, -1], [1, 0]]
    ds2 = [[0, 1], [-1, 0]]
    l = 1
    cur_pos = player
    flat_list = []
    while l < n:
        if l % 2 == 0:
            dss = ds2
        else:
            dss = ds1
        for ds in dss:
            t = 0
            while t < l:
                cur_pos = [cur_pos[0] + ds[0], cur_pos[1] + ds[1]]
                if grid[cur_pos[0]][cur_pos[1]] != 0:
                    flat_list.append(grid[cur_pos[0]][cur_pos[1]])
                t += 1
        l += 1
    for j in range(n-2, -1, -1):
        if grid[0][j] != 0:
            flat_list.append(grid[0][j])

    return flat_list


def initialize_map():
    global grid
    grid = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    return


def fill_map(monsters):
    ds1 = [[0, -1], [1, 0]]
    ds2 = [[0, 1], [-1, 0]]
    l = 1
    cur_pos = player
    mon_idx = 0
    fill_finished = False

    initialize_map()

    while l < n and not fill_finished:
        if l % 2 == 0:
            dss = ds2
        else:
            dss = ds1
        for ds in dss:
            t = 0
            while t < l and not fill_finished:
                cur_pos = [cur_pos[0] + ds[0], cur_pos[1] + ds[1]]
                grid[cur_pos[0]][cur_pos[1]] = monsters[mon_idx]
                t += 1
                mon_idx += 1
                if mon_idx >= len(monsters):
                    fill_finished = True
                    break
        l += 1

    if not fill_finished:
        for j in range(n-2, -1, -1):
            grid[0][j] = monsters[mon_idx]
            mon_idx += 1
            if mon_idx >= len(monsters):
                break


def remove(monsters):
    global score
    temp_list = []
    is_removed = False
    i = 0
    while i < len(monsters) - 1:
        if monsters[i] == monsters[i + 1]:
            count = 1
            j = i + 1
            while  j < len(monsters) and monsters[i] == monsters[j]:
                j += 1
                count += 1
            if count >= 4:
                score += monsters[i] * count
                i = j
                is_removed = True
            else:
                for x in range(i, j):
                    temp_list.append(monsters[x])
                i = j
            if i == len(monsters) - 1:
                temp_list.append(monsters[i])
        else:
            temp_list.append(monsters[i])
            i += 1
            if i == len(monsters) - 1:
                temp_list.append(monsters[i])

    return is_removed, temp_list


def generate(monsters):
    temp_list = []
    i = 0
    while i < len(monsters) - 1:
        if monsters[i] == monsters[i + 1]:
            count = 1
            j = i + 1
            while  j < len(monsters) and monsters[i] == monsters[j]:
                j += 1
                count += 1
            temp_list.append(count)
            temp_list.append(monsters[i])
            i = j
            if i == len(monsters) - 1:
                temp_list.append(1)
                temp_list.append(monsters[i])
        else:
            temp_list.append(1)
            temp_list.append(monsters[i])
            i += 1
            if i == len(monsters) - 1:
                temp_list.append(1)
                temp_list.append(monsters[i])

    if len(temp_list) > pow(n, 2):
        return temp_list[:pow(n, 2) - 1]
    return temp_list





################################################################
score = 0
game()
print(score)