n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

drs = [
    [[0, -1], [1, 0]],
    [[0, 1], [-1, 0]]
]

def simulate():
    distance = 1
    pos = [n//2, n//2]
    while distance != n:
        if distance % 2 == 1:
            pos = move(pos, drs[0][0], distance)
            pos = move(pos, drs[0][1], distance)
        else:
            pos = move(pos, drs[1][0], distance)
            pos = move(pos, drs[1][1], distance)
        distance += 1
    move(pos, drs[0][0], n - 1)

def move(p, d, l):
    # ex) d = [0, -1]
    length = 0
    next_pos = [-1, -1]
    cur_pos = p
    while length < l:
        next_pos = [cur_pos[0] + d[0], cur_pos[1] + d[1]]
        clean(next_pos, d)
        cur_pos = next_pos
        length += 1

    return next_pos

# D, R, U, L
blow_areas = [
    [   # D
        [0, 0, 0, 0, 0],
        [0, 0.01, 0, 0.01, 0],
        [0.02, 0.07, 0, 0.07, 0.02],
        [0, 0.1, 0.55, 0.1, 0],
        [0, 0, 0.05, 0, 0]
    ],
    [   # R
        [0, 0, 0.02, 0, 0],
        [0, 0.01, 0.07, 0.1, 0],
        [0, 0, 0, 0.55, 0.05],
        [0, 0.01, 0.07, 0.1, 0],
        [0, 0, 0.02, 0, 0]
    ],
    [   # U
        [0, 0, 0.05, 0, 0],
        [0, 0.1, 0.55, 0.1, 0],
        [0.02, 0.07, 0, 0.07, 0.02],
        [0, 0.01, 0, 0.01, 0],
        [0, 0, 0, 0, 0]
    ],
    [   # L
        [0, 0, 0.02, 0, 0],
        [0, 0.1, 0.07, 0.01, 0],
        [0.05, 0.55, 0, 0, 0],
        [0, 0.1, 0.07, 0.01, 0],
        [0, 0, 0.02, 0, 0]
    ]
]

def dictionary(key):
    val = -1
    if key == [1, 0]:
        val = 0
    if key == [0, 1]:
        val = 1
    if key == [-1, 0]:
        val = 2
    if key == [0, -1]:
        val = 3
    return val

def clean(cur_pos, direct):
    global total_ob_dust
    cur_areas = blow_areas[dictionary(direct)]
    cur_dust = grid[cur_pos[0]][cur_pos[1]]
    rest_dust = cur_dust
    a_pos = []

    for i in range(5):
        for j in range(5):
            g_i, g_j = cur_pos[0] + i - 2, cur_pos[1] + j - 2
            temp_dust = int(cur_areas[i][j] * cur_dust)
            if 0 <= g_i < n and 0 <= g_j < n:
                if cur_areas[i][j] == 0.55:
                    a_pos = [g_i, g_j, True]
                    continue
                grid[g_i][g_j] += temp_dust
                rest_dust -= temp_dust
            else:
                if cur_areas[i][j] == 0.55:
                    a_pos = [g_i, g_j, False]
                    continue
                total_ob_dust += temp_dust
                rest_dust -= temp_dust

    grid[cur_pos[0]][cur_pos[1]] = 0

    if a_pos:
        if a_pos[2]:
            grid[a_pos[0]][a_pos[1]] += rest_dust
        else:
            total_ob_dust += rest_dust

    return

total_ob_dust = 0
simulate()
print(total_ob_dust)