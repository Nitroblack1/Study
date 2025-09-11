n, m = map(int, input().split())
# 자동차 초기 좌표 x, y / 초기 방향 d
x, y, d = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(n)]

# 북 : 0 / 동 : 1 / 남 : 2 / 서 : 3
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3

# 문제상 좌회전만 존재한다.
def rotate():
    if d == NORTH:
        return WEST
    else:
        return d - 1

# 주어진 방향으로 이동. 방문한 도로는 -1로 변경하여 재방문 제한.
def can_move(di, r):
    if di == NORTH and x - r >= 0 and road[x - r][y] == 0:
        return True
    elif di == SOUTH and x + r < n and road[x + r][y] == 0:
        return True
    elif di == EAST and y + r < m and road[x][y + r] == 0:
         return True
    elif di == WEST and y - r >= 0 and road[x][y - r] == 0:
          return True
    else:
        return False

def can_roll_back():
    if d == NORTH and x + 1 >= 0 and road[x + 1][y] != 1:
        return True
    elif d == SOUTH and x - 1 < n and road[x - 1][y] != 1:
        return True
    elif d == EAST and y - 1 < m and road[x][y - 1] != 1:
         return True
    elif d == WEST and y + 1 >= 0 and road[x][y + 1] != 1:
          return True
    else:
        return False


def move(r):
    global x, y
    if d == NORTH:
        x -= r
        road[x][y] = -1
    elif d == SOUTH:
        x += r
        road[x][y] = -1
    elif d == EAST:
        y += r
        road[x][y] = -1
    elif d == WEST:
        y -= r
        road[x][y] = -1
    else:
        return False

road[x][y] = -1
area = 1
while True:
    count = 0
    d = rotate()
    # 현재 방향으로 전진할 수 있거나 4방향 다 탐색했을 때 탈출
    while not can_move(d, 1) and count < 3:
        d = rotate()
        count += 1
    if can_move(d, 1):
        move(1)
        area += 1
    else:
        if can_roll_back():
            move(-1)
        else:
            break

print(area)