n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# grid 범위 체크
def is_grid(i, j):
    if 0 <= i < n and 0 <= j < m:
        return True
    return False

# k 초과 여부 체크
def is_higher(i, j, k):
    if grid[i][j] > k:
        return True
    return False

# DFS
visited = [[False] * m for _ in range(n)]
dis, djs = [0,1,0,-1], [1,0,-1,0]   # R, D, L, U
def dfs(i, j):
    visited[i][j] = True

    for di, dj in zip(dis, djs):
        new_i, new_j = i + di, j + dj
        if is_grid(new_i, new_j) and is_higher(new_i, new_j, k) and not visited[new_i][new_j]:
            dfs(new_i, new_j)


max_safe_area = 0
max_k = 1
max_height = 0

for row in grid:
    max_height = max(max_height, max(row))


for k in range(1, max_height):
    safe_area = 0
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if is_higher(i, j, k) and not visited[i][j]:
                dfs(i, j)
                safe_area += 1

    if max_safe_area < safe_area:
        max_safe_area = safe_area
        max_k = k

print(max_k, max_safe_area)