n, m, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]


def simulate():
    for _ in range(t):
        diffuse()
        blow()
    return


def diffuse():
    temp_grid = [[0] * m for _ in range(n)]
    temp_num = [[0] * m for _ in range(n)]

    dis, djs = [0, 1, 0, -1], [1, 0, -1, 0]

    for i in range(n):
        for j in range(m):
            if room[i][j] < 1:
                continue
            for di, dj in zip(dis, djs):
                ni, nj = i + di, j + dj
                # if it is in range and not wind
                if (0 <= ni < n and 0 <= nj < m) and room[ni][nj] != -1:
                    temp_grid[ni][nj] += room[i][j] // 5
                    # how many num should it be divided
                    temp_num[i][j] += 1

    for i in range(n):
        for j in range(m):
            room[i][j] = room[i][j] - ((room[i][j] // 5) * temp_num[i][j]) + temp_grid[i][j]

    return


def blow():
    for i in range(n):
        if room[i][0] == -1:
            rotate(i, -1)
            rotate(i+1, 1)
            return
    return

def rotate(i, d):
    if d == -1:
        for left in range(i - 1, 0, -1):
            room[left][0] = room[left - 1][0]
        for top in range(m - 1):
            room[0][top] = room[0][top + 1]
        for right in range(0, i):
            room[right][m - 1] = room[right + 1][m - 1]
        for bottom in range(m - 1, 1, -1):
            room[i][bottom] = room[i][bottom - 1]
        room[i][1] = 0

    if d == 1:
        for left in range(i + 1, n - 1):
            room[left][0] = room[left + 1][0]
        for bottom in range(0, m - 1):
            room[n - 1][bottom] = room[n - 1][bottom + 1]
        for right in range(n - 1, i, -1):
            room[right][m - 1] = room[right - 1][m - 1]
        for top in range(m - 1, 1, -1):
            room[i][top] = room[i][top - 1]
        room[i][1] = 0


def get_total_dusts():
    total = 0
    for i in range(n):
        for j in range(m):
            total += room[i][j]

    return total + 2



simulate()
print(get_total_dusts())