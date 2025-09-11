from collections import deque

N, L, R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

q = deque()
dxs = [1,0,-1,0]
dys = [0,1,0,-1]

def is_range(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False

def bfs(x,y):
    q.append((x,y))
    union = [(x, y)]
    while q:
        a, b = q.popleft()
        for dx, dy in zip(dxs, dys):
            na, nb = a + dx, b + dy
            if not is_range(na, nb) or visited[na][nb]:
                continue
            if R >= abs(grid[a][b] - grid[na][nb]) >= L:
                visited[na][nb] = 1
                q.append((na,nb))
                union.append((na,nb))
    if len(union) <= 1:
        return 0
    result = sum(grid[a][b] for a, b in union) // len(union)
    for a, b in union:
        grid[a][b] = result
    return 1

day = 0
while 1:
    stop = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = True
                stop += bfs(i,j)
    if stop == 0:
        break
    day += 1

print(day)