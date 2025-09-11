n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]


def dfs(i, j):
    if i == n-1 and j == m-1:
        return 1

    # move : down > right
    dis = [1, 0]
    djs = [0, 1]

    for di, dj in zip(dis, djs):
        new_i, new_j = i + di, j + dj

        if can_go(new_i, new_j):
            visited[new_i][new_j] = True
            if dfs(new_i, new_j):
                return 1
    return 0


def can_go(i, j):
    if 0 <= i < n and 0 <= j < m:
        if not visited[i][j] and grid[i][j] == 1:
            return True
    return False


visited[0][0] = 1
print(int(dfs(0,0) == 1))