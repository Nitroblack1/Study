from collections import deque

# 한 칸에는 몬스터가 최대 한 개만 존재.
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
# r, c, lv
robot = [-1, -1, 2]

# game state check
finished = False

# overall time
time = 0

# get robot position
for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            robot[0], robot[1] = i, j
            grid[i][j] = 0


def game():
    global finished
    # current kill num in current level
    exp = 0
    while not finished:
        target = hunt()
        if target is None:
            finished = True
        else:
            # exp increase when kill monster
            kill(target)
            exp += 1

            # if robot killed as many as its level, lv up.
            if exp == robot[2]:
                robot[2] += 1
                exp = 0

# find nearest monster following all conditions, using BFS
def hunt():
    global time

    # print('robot pos is : ', robot)
    q = deque()
    visited = [[False] * n for _ in range(n)]
    kill_list = []
    # up first, left second.
    search = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    q.append((robot[0], robot[1], 0))
    min_nd = n*n

    while q:
        ci, cj, cd = q.popleft()
        visited[ci][cj] = True
        for d in search:
            ni, nj, nd = ci + d[0], cj + d[1], cd + 1
            # if it is in grid
            if 0 <= ni < n and 0 <= nj < n:
                # and if it can pass (it includes two cases, lower monster or road)
                if not visited[ni][nj] and grid[ni][nj] <= robot[2]:
                    # if it is monster and lv is lower than robot
                    if grid[ni][nj] != 0 and grid[ni][nj] < robot[2] and min_nd >= nd:
                        min_nd = nd
                        kill_list.append((ni, nj, nd))
                        visited[ni][nj] = True
                    # else, it is just a road
                    else:
                        q.append((ni, nj, nd))
                        visited[ni][nj] = True
                # if it can't pass
                else:
                    visited[ni][nj] = True

    if kill_list:
        kill_list.sort(key=lambda x: (x[2], x[0], x[1]))
        # print(kill_list)
        time += kill_list[0][2]
        # print('killed : ', kill_list[0], 'time is : ', time)
        return kill_list[0]

    # if there's no monster available to kill, return None
    return None

def kill(target):
    # move to monster
    robot[0], robot[1] = target[0], target[1]
    # kill monster
    grid[target[0]][target[1]] = 0


game()
print(time)