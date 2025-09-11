from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

q = deque()
# move condition check
def can_go(i, j):
    if 0 <= i < n and 0 <= j < m:
        if not visited[i][j] and grid[i][j] == 1:
            return True
    return False


# bfs
def bfs(i, j):
    visited[i][j] = True
    q.append((i, j))

    # move
    dis, djs = [1, 0, -1, 0], [0, 1, 0, -1]

    while q:
        i, j = q.popleft()

        for di, dj in zip(dis, djs):
            ni, nj = i + di, j + dj
            if can_go(ni, nj):
                if ni == n-1 and nj == m-1:
                    return True
                visited[ni][nj] = True
                q.append((ni, nj))
    return False


print(int(bfs(0,0)))