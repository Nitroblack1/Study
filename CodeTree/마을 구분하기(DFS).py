n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

def dfs(i, j):
    # check visited vertex
    visited[i][j] = True

    global people

    # move : right / down / left / up
    dis, djs = [0,1,0,-1], [1,0,-1,0]

    for di, dj in zip(dis, djs):
        new_i, new_j = di + i, dj + j
        if is_ingrid(new_i, new_j) and can_go(new_i, new_j):
            people += 1
            dfs(new_i, new_j)


# 0. is inside grid
def is_ingrid(i, j):
    if 0 <= i < n and 0 <= j < n:
        return True
    return False


# 1. is not wall
# 2. is not visited
def can_go(i, j):
    if grid[i][j] != 0 and not visited[i][j]:
        return True
    return False


village = 0
peoples = []
for i in range(n):
    for j in range(n):
        if is_ingrid(i, j) and can_go(i, j):
            people = 1
            dfs(i, j)
            village += 1
            peoples.append(people)

peoples.sort()
print(village)
for p in peoples:
    print(p)