# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

U, D, L, R = [-1, 0], [1, 0], [0, -1], [0, 1]
pipe_dict = {
    1: [U, D, L, R],    # +
    2: [U, D],          # ㅣ
    3: [L, R],          # ㅡ
    4: [U, R],          # ㄴ
    5: [R, D],          # r
    6: [L, D],          # ㄱ
    7: [L, U]           # ㅢ
}

def debug(board):
    for i in board:
        for j in i:
            print(int(j), end=" ")
        print()


def inb(i, j):
    return 0 <= i < n and 0 <= j < m


def bfs(i, j):
    q = deque()
    visited = [
        [False for _ in range(m)]
        for _ in range(n)
    ]

    time, count = 1, 1
    visited[i][j] = True
    q.append((i, j, time))
    while q and time < l:
        ci, cj, time = q.popleft()
        for di, dj in pipe_dict.get(grid[ci][cj]):
            ni, nj = ci + di, cj + dj
            if inb(ni, nj) and not visited[ni][nj] and grid[ni][nj] != 0:
                nds = pipe_dict.get(grid[ni][nj])
                for ndi, ndj in nds:
                    if ndi * -1 == di and ndj * -1 == dj:
                        q.append((ni, nj, time + 1))
                        if time < l:
                            count += 1
                        visited[ni][nj] = True

    return count


T = int(input())
for test_case in range(1, T + 1):
    n, m, r, c, l = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    ans = bfs(r, c)

    print(f'#{test_case} {ans}')