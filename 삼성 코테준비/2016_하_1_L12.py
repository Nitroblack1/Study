# Simulation
n, m, x, y, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

EAST = 1
WEST = 2
NORTH = 3
SOUTH = 4

rolls = list(map(int, input().split()))

# grid를 벗어나는 시도는 무시하며, 출력도 하지 않는다.
# 이동할 때마다 정육면체의 상단 면에 쓰여져 있는 숫자를 출력하라.

cube = [0, 0, 0, 0, 0, 0]
# 정육면체 각 면 매직 넘버 부여
U, F, D, B, R, L = 0, 1, 2, 3, 4, 5


def roll(direction):
    global x, y
    if direction == EAST:
        temp = cube[L]
        cube[L] = cube[D]
        cube[D] = cube[R]
        cube[R] = cube[U]
        cube[U] = temp
        # 주사위 위치 업데이트
        y += 1
    if direction == WEST:
        temp = cube[U]
        cube[U] = cube[R]
        cube[R] = cube[D]
        cube[D] = cube[L]
        cube[L] = temp
        # 주사위 위치 업데이트
        y -= 1
    if direction == SOUTH:
        temp = cube[B]
        for s in range(3, 0, -1):
            cube[s] = cube[s-1]
        cube[U] = temp
        x += 1
    if direction == NORTH:
        temp = cube[U]
        for b in range(3):
            cube[b] = cube[b+1]
        cube[B] = temp
        x -= 1
    return cube[U]

# 해당 방향으로 굴릴 수 있는가?
def can_roll(direction, cube_x, cube_y):
    if direction == EAST:
        if cube_y + 1 < m:
            return True
    if direction == WEST:
        if cube_y - 1 >= 0:
            return True
    if direction == SOUTH:
        if cube_x + 1 < n:
            return True
    if direction == NORTH:
        if cube_x - 1 >= 0:
            return True
    return False

# 주사위 굴린 후 cube[D]와 맵 간의 상호작용
def update():
    if grid[x][y] == 0:
        grid[x][y] = cube[D]
    else:
        cube[D] = grid[x][y]
        grid[x][y] = 0


# 굴릴 수 있는가 > 굴린 후 cube[U]는 출력, cube[D]는 맵과 상호작용.
for i in range(k):
    if can_roll(rolls[i], x, y):
        roll(rolls[i])
        update()
        print(cube[U])