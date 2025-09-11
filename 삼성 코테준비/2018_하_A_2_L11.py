from collections import deque

n, l, r = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


def egg_search(x, y):
    global updated, visited
    # bfs 기본 세팅
    q = deque()
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    mixed_area = []

    q.append((x, y))
    mixed_area.append((x, y))
    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if can_go(cx, cy, nx, ny) and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                mixed_area.append((nx, ny))

    # 한 번이라도 갱신됐다면 not stop
    if len(mixed_area) > 1:
        updated = True
        mix(mixed_area)
        # for v in visited:
        #     for e in v:
        #         print(e, end=" ")
        #     print()
        # print()

# 그리드 내부인가? l 이상 r 이하의 차이가 나는가?
def can_go(cx, cy, nx, ny):
    if 0 <= nx < n and 0 <= ny < n:
        if l <= abs(grid[cx][cy] - grid[nx][ny]) <= r:
            return True
    return False


def mix(targets):
    mixing = 0
    for target in targets:
        mixing += grid[target[0]][target[1]]

    mixed_result = mixing // len(targets)
    for target in targets:
        grid[target[0]][target[1]] = mixed_result


answer = 0
updated = True
visited = [[False] * n for _ in range(n)]

while updated:
    visited = [[False] * n for _ in range(n)]
    updated = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                egg_search(i, j)
    if updated:
        answer += 1

print(answer)