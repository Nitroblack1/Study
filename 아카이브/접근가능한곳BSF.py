from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

start_points = []
for i in range(k):
    start_points.append(list(map(int, input().split())))

def is_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False

def can_go(x, y):
    if not visited[x][y] and grid[x][y] == 0:
        return True
    else:
        return False

def bfs(x, y):
    if can_go(x, y):
        move_count = 1
    else:
        move_count = 0
    q = deque()
    visited[x][y] = True
    q.append((x,y))
    dxs = [1,0,-1,0]
    dys = [0,-1,0,1]

    while q:
        current_node = q.popleft()
        for dx, dy in zip(dxs, dys):
            next_x, next_y = current_node[0] + dx, current_node[1] + dy
            if is_range(next_x, next_y) and can_go(next_x, next_y):
                move_count += 1
                visited[next_x][next_y] = True
                q.append((next_x, next_y))

    return move_count

available_num = 0

for start_point in start_points:
    available_num += bfs(start_point[0] - 1, start_point[1] - 1)

print(available_num)