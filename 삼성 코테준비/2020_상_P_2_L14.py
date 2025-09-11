# 1칸당 1 소비, 승객 목적지로 이동시킨 동시에 소비량 * 2 만큼 충전.
# 이동 도중 배터리가 모두 소모되면 즉시 종료.
# 승객을 목적지에 이동시킨 동시에 배터리가 모두 소모되면 배터리 충전 우선, 운행 가능.
# 마지막 승객을 태워주고 운행 종료하는 순간에도 충전 이뤄짐.
## 즉, 우선순위 : [이동] > [소비] > [충전]? > [종료 체크; if battery == 0]
# BFS 우선 순위 : 상 > 좌 > ...
##############################################################

### 도착지가 겹치는 경우 고려해야 함.

from collections import deque

n, m, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

car = list(map(int, input().split()))
car[0] -= 1
car[1] -= 1
clients = [list(map(int, input().split())) for _ in range(m)]

goal_map = [
    [[] for _ in range(n)] for _ in range(n)
]

for row in range(m):
    for col in range(4):
        clients[row][col] -= 1

for row in range(n):
    for col in range(n):
        for num in range(m):
            if row == clients[num][0] and col == clients[num][1]:
                grid[row][col] = -1 * (num + 2)
                goal_map[clients[num][2]][clients[num][3]].append(num + 2)

client_num = m
is_impossible = False

# 만약 그리드 안 + 도로면
def can_go(i, j):
    if 0 <= i < n and 0 <= j < n:
        if grid[i][j] != 1:
            return True
    return False


def bfs(car_pos):
    global c, client_num, is_impossible

    if client_num == 0:
        return

    q = deque()
    q.append((car_pos[0], car_pos[1], 0))

    visited = [[False] * n for _ in range(n)]
    # 상, 좌, 하, 우
    dis, djs = [-1, 0, 0, 1], [0, -1, 1, 0]
    cl_list = []
    cur_dis = 1000

    visited[car_pos[0]][car_pos[1]] = True
    # find client
    while q:
        ci, cj, distance = q.popleft()
        # 연료 바닥나면 pass
        if c - distance <= 0:
            continue
        # 만약 승객을 찾았다면
        if grid[ci][cj] < 0 and distance <= cur_dis:
            # 후보지에 추가하고 최단거리 기록
            cur_dis = distance
            cl_list.append([ci, cj])
            # print('cl added ', cl_list)

        for di, dj in zip(dis, djs):
            ni, nj = ci + di, cj + dj
            if can_go(ni, nj) and not visited[ni][nj]:
                q.append((ni, nj, distance + 1))
                visited[ni][nj] = True

    if len(cl_list) == 0:
        is_impossible = True
        return

    if cl_list:
        client_num -= 1

    cl_list.sort(key=lambda x: [x[0], x[1]])
    # 연료 깎고
    c -= cur_dis
    # 차 해당 위치로 이동
    car_pos[0], car_pos[1] = cl_list[0][0], cl_list[0][1]
    # 목적지 설정 (-1, -2, ...)
    goal = -1 * grid[cl_list[0][0]][cl_list[0][1]]
    # 승객 태웠으므로 지도에서 삭제
    grid[cl_list[0][0]][cl_list[0][1]] = 0
    # print('pick up ', goal - 1, 'at ', car, '/ left fuel : ', c, 'goal is ', goal - 1)


    # find destination
    q = deque()
    q.append((car_pos[0], car_pos[1], 0))
    visited = [[False] * n for _ in range(n)]
    visited[car_pos[0]][car_pos[1]] = True
    # 상, 좌, 하, 우
    dis, djs = [-1, 0, 1, 0], [0, -1, 0, 1]

    while q:
        ci, cj, distance = q.popleft()
        if c - distance == 0:
            is_impossible = True
            # print('impossible, ', ci, cj, c, distance)
            return

        for di, dj in zip(dis, djs):
            ni, nj = ci + di, cj + dj
            if not can_go(ni, nj) or visited[ni][nj]:
                continue
            # 목적지면
            for destination in goal_map[ni][nj]:
                if destination == goal:
                    c += distance + 1
                    # goal_map[ni][nj] = 0
                    # print('arrived, fuel : ', c)
                    bfs([ni, nj])
                    return
            q.append((ni, nj, distance + 1))
            visited[ni][nj] = True

    is_impossible = True
    return


###########################################################
bfs(car)

if is_impossible:
    print(-1)
else:
    print(c)