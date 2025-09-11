from collections import deque

# 2^n 그리드 / q번 시전
N, Q = map(int, input().split())
grid_len = 2**N

# 얼음판 형성
grid = [list(map(int, input().split())) for _ in range(grid_len)]

# 각 시행별 레벨
L = list(map(int, input().split()))

# 탐색 방향 (좌,하,우,상)
dxs = [1,0,-1,0]
dys = [0,-1,0,1]

# 그리드 범위 안인지 확인
def is_inbound(x, y):
    if 0 <= x < grid_len and 0 <= y < grid_len:
        return True
    return False

# 얼음이 있는지 확인
def is_ice(x, y):
    if grid[x][y] > 0:
        return True
    return False


# 각 레벨별 rotate
def rotate(l):
    global grid
    temp = [[0] * grid_len for _ in range(grid_len)]
    part_len = 2**l
    for ii in range(0, grid_len, part_len):
        for jj in range(0, grid_len, part_len):
            for i in range(part_len):
                for j in range(part_len):
                    temp[ii + j][jj + (part_len-i-1)] = grid[ii + i][jj + j]

    grid = temp


# 인접하지 않은 얼음덩어리들을 찾아 -1을 해줌.
def melt_ice():
    melt_index = set()
    for i in range(grid_len):
        for j in range(grid_len):
            near = 0
            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy
                if is_inbound(nx, ny) and grid[nx][ny] > 0:
                    near += 1
            if near < 3 and grid[i][j] > 0:
                melt_index.add((i, j))
    for i, j in melt_index:
        if grid[i][j] > 0:
            grid[i][j] -= 1


# 각 지점에서 BFS로 탐색하여 최대 넓이를 돌려줌.
def get_max_area():
    visited = [[False] * grid_len for _ in range(grid_len)]
    max_area = 0

    for i in range(grid_len):
        for j in range(grid_len):
            if not visited[i][j] and grid[i][j] > 0:
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                area = 1

                while q:
                    x, y = q.popleft()
                    for dx, dy in zip(dxs, dys):
                        nx, ny = x + dx, y + dy
                        if is_inbound(nx, ny) and not visited[nx][ny] and grid[nx][ny] > 0:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            area += 1
                max_area = max(max_area, area)

    return max_area


def total_ice():
    total = 0
    for i in range(grid_len):
        for j in range(grid_len):
            total += grid[i][j]
    return total

######################################################################

# Main fn
# 총 Q번 시전
for i in range(Q):
    # 먼저 2^L에 맞게 나눈 부분 격자들에 대해 시계 90도 회전을 해주고
    rotate(L[i])
    # 인접하지 않은 얼음이 있는 칸들에 대해 -1을 해준다.
    melt_ice()

# Q회 시전 후 반영된 그리드에 대해 얼음 총량과 최대 크기를 구한다.
print(total_ice())
print(get_max_area())