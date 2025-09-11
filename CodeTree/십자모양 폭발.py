n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
# explode numbers
def explode(i, j):
    # right, left, up, down
    dis = [0,0,-1,1]
    djs = [1,-1,0,0]

    # size
    l = grid[i][j]
    for di, dj in zip(dis, djs):
        for d in range(l):
            if 0 <= i + di * d < n and 0 <= j + dj * d < n:
                grid[i + di*d][j + dj*d] = 0


# gravity on
def gravity():
    temp = [[0] * n for _ in range(n)]
    for j in range(n):
        temp_i = n-1
        for i in range(n-1, -1, -1):
            if grid[i][j] != 0:
                temp[temp_i][j] = grid[i][j]
                temp_i -= 1

    return temp

explode(r-1, c-1)
grid[:] = gravity()

for row in grid:
    for element in row:
        print(element, end=" ")
    print()