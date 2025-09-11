n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

# search condition
def can_go(i, j):
    if 0 <= i < n and 0 <= j < n:
        if not visited[i][j]:
            return True
    return False


# dfs
def dfs(i, j):
    visited[i][j] = True
    global block_size

    # move
    dis, djs = [0,1,0,-1], [1,0,-1,0]

    for di, dj in zip(dis, djs):
        new_i, new_j = i + di, j + dj

        if can_go(new_i, new_j) and grid[new_i][new_j] == grid[i][j]:
            dfs(new_i, new_j)
            block_size += 1

ppuyo = 0
max_block_size = 0
for i in range(n):
    for j in range(n):
        block_size = 1
        dfs(i, j)
        max_block_size = max(block_size, max_block_size)
        if block_size >= 4:
            ppuyo += 1

print(ppuyo, max_block_size)
