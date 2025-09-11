# 접근
# 1. 방화벽 3개를 세울 수 있는 모든 경우의 수를 BT로 알아내어 맵을 설정
# 2. BFS로 영역 범위 구하여 최댓값 계속 갱신, 해당값 리턴
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
fires = []
guard_walls = 0
answer = 0
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            # 최초 불 좌표 기록
            fires.append((i, j))
        if grid[i][j] == 1:
            guard_walls += 1


# 방화벽 3개를 설치하는 모든 경우의 수.
# 3개를 설치한 경우 바로 BFS 탐색 시전
def create_map(g):
    burned_area = 0
    global answer, visited
    if g == 3:
        temp = [[0] * m for _ in range(n)]
        for x in range(n):
            for y in range(m):
                temp[x][y] = grid[x][y]

        visited = [[False] * m for _ in range(n)]
        for fire in fires:
            burned_area += bfs(fire)

        answer = max(answer, m*n - burned_area - guard_walls - 3)
        return

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                grid[i][j] = 1
                create_map(g+1)
                grid[i][j] = 0


# 방화 좌표에 대해 bfs. idx : tuple(i, j)
q = deque()

def can_go(x, y):
    if 0 <= x < n and 0 <= y < m:
        if not visited[x][y] and grid[x][y] == 0:
            return True
    return False

def bfs(idx):
    count = 1
    visited[idx[0]][idx[1]] = True
    # 우, 하, 좌, 상
    dis, djs = [0, 1, 0, -1], [1, 0, -1, 0]
    q.append(idx)

    while q:
        a, b = q.popleft()
        for di, dj in zip(dis, djs):
            new_i, new_j = a + di, b + dj
            if can_go(new_i, new_j):
                q.append((new_i, new_j))
                visited[new_i][new_j] = True
                count += 1
    return count


create_map(0)
print(answer)