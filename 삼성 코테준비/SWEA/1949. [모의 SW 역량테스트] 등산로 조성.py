dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def dfs(x, y, dist, k_left):
    global ans
    ans = max(ans, dist)

    visited[x][y] = 1
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if mountain[nx][ny] < mountain[x][y]:
                dfs(nx, ny, dist + 1, k_left)
            elif k_left > 0 and mountain[nx][ny] - k_left < mountain[x][y]:
                tmp = mountain[nx][ny]
                mountain[nx][ny] = mountain[x][y] - 1  # 딱 한 번, 경로 내에서만 임시 절단
                dfs(nx, ny, dist + 1, 0)
                mountain[nx][ny] = tmp
    visited[x][y] = 0

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    top = max(max(row) for row in mountain)

    ans = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == top:
                dfs(i, j, 1, K)
    print(f'#{tc} {ans}')