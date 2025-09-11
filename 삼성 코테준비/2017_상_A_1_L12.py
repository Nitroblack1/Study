n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


# blocks area
S_type = [
    [[0,0], [0,1], [1,0], [1,1]]
]

I_type = [
    [[0,0], [0,1], [0,2], [0,3]],
    [[0,0], [1,0], [2,0], [3,0]]
]

N_type = [
    [[0,0], [1,0], [1,1], [2,1]],
    [[0,1], [0,2], [1,0], [1,1]],
    [[0,0], [0,1], [1,1], [1,2]],
    [[0,1], [1,1], [1,0], [2,0]]
]

L_type = [
    [[0,0], [1,0], [2,0], [2,1]],
    [[1,0], [1,1], [1,2], [0,2]],
    [[0,0], [0,1], [0,2], [1,0]],
    [[0,0], [0,1], [1,1], [2,1]],
    [[0,1], [1,1], [2,1], [2,0]],
    [[0,0], [1,0], [1,1], [1,2]],
    [[0,0], [0,1], [1,0], [2,0]],
    [[0,0], [0,1], [0,2], [1,2]]
]

T_type = [
    [[0,0], [0,1], [0,2], [1,1]],
    [[0,1], [1,0], [1,1], [1,2]],
    [[0,1], [1,0], [1,1], [2,1]],
    [[0,0], [1,0], [1,1], [2,0]]
]

types = [S_type, I_type, N_type, L_type, T_type]

def calculate(x, y, t):
    cur_max_block_sum = -1
    for shape in t:
        block_sum = 0
        for index in shape:
            cur_x, cur_y = x + index[0], y + index[1]
            if 0 <= cur_x < n and 0 <= cur_y < m:
                block_sum += grid[cur_x][cur_y]
            else:
                break
        cur_max_block_sum = max(cur_max_block_sum, block_sum)
    return cur_max_block_sum

max_sum = 0
for i in range(n, -1, -1):
    for j in range(m, -1, -1):
        for type in types:
            max_sum = max(max_sum, calculate(i, j, type))


print(max_sum)