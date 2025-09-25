from collections import deque

n, t = map(int, input().split())
temp = [list(input()) for _ in range(n)]
power = [list(map(int, input().split())) for _ in range(n)]

grid = [
    [set() for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        grid[i][j].add(temp[i][j])


def debug(board):
    for r in board:
        for c in r:
            print(c, end=" ")
        print()
    print()


def inb(r, c):
    return 0 <= r < n and 0 <= c < n


def breakfast():
    for r in range(n):
        for c in range(n):
            power[r][c] += 1


def lunch():
    visited = [
        [False for _ in range(n)]
        for _ in range(n)
    ]
    lds = []

    for r in range(n):
        for c in range(n):
            if not visited[r][c]:
                visited[r][c] = True
                lds.append(bfs(r, c, visited))
    return lds


def bfs(r, c, v):
    q = deque()
    dis, djs = [0, 1, 0, -1], [1, 0, -1, 0]
    leader = (r, c)
    member = 1

    q.append((r, c))
    while q:
        ci, cj = q.popleft()
        for di, dj in zip(dis, djs):
            ni, nj = ci + di, cj + dj
            if inb(ni, nj) and not v[ni][nj] and grid[ci][cj] == grid[ni][nj]:
                v[ni][nj] = True
                q.append((ni, nj))
                member += 1
                # 만약 n이 기존 leader보다 더 강하면
                if power[leader[0]][leader[1]] < power[ni][nj]:
                    # 리더가 아니면 1 헌납
                    power[leader[0]][leader[1]] -= 1
                    leader = (ni, nj)

                # 파워가 같다면, r min, c min을 리더로 설정한다.
                elif power[leader[0]][leader[1]] == power[ni][nj] and leader > (ni, nj):
                    # 리더가 아니면 1 헌납
                    power[leader[0]][leader[1]] -= 1
                    leader = (ni, nj)
                else:
                    # 리더가 아니면 1 헌납
                    power[ni][nj] -= 1

    power[leader[0]][leader[1]] += member - 1
    return leader


def dinner(lds):
    # ready
    ready_lds = []
    # 방어 상태여부 맵, 저녁 시간마다 초기화
    is_attacked = [
        [False for _ in range(n)]
        for _ in range(n)
    ]

    for l in lds:
        ready_lds.append([len(grid[l[0]][l[1]]), power[l[0]][l[1]], l[0], l[1]])
    ready_lds.sort(key=lambda x: [x[0], -x[1], x[2], x[3]])

    # attack
    dir_dict = {
        0: [-1, 0],
        1: [1, 0],
        2: [0, -1],
        3: [0, 1]
    }
    for l in ready_lds:
        # 만약 방어상태라면 pass
        if is_attacked[l[2]][l[3]]:
            continue
        # 간절함 = B - 1
        desp = power[l[2]][l[3]] - 1
        # B = 1
        power[l[2]][l[3]] = 1
        ds = dir_dict.get(l[1] % 4)
        distance = 1
        cr, cc = l[2], l[3]
        while desp > 0 and inb(cr, cc):
            nr, nc = cr + ds[0] * distance, cc + ds[1] * distance
            if inb(nr, nc) and grid[cr][cc] != grid[nr][nc]:
                # 강한 전파
                if desp > power[nr][nc]:
                    # 동화
                    grid[nr][nc] = grid[cr][cc]
                    # desp 깎음
                    desp -= (power[nr][nc] + 1)
                    # 대상 신앙심 + 1
                    power[nr][nc] += 1
                    # 방어모드 on
                    is_attacked[nr][nc] = True
                # 약한 전파
                else:
                    # 관심 갖기
                    grid[nr][nc] = grid[nr][nc].union(grid[cr][cc])
                    # 대상 신앙심 + desp
                    power[nr][nc] += desp
                    # desp 제거
                    desp = 0
                    # 방어모드 on
                    is_attacked[nr][nc] = True
                    # desp = 0이므로 break : 최적화 요소
                    break

            # 좌표 갱신
            cr, cc = nr, nc


def get_sum():
    foods = [{"T", "C", "M"}, {"T", "C"}, {"T", "M"}, {"C", "M"}, {"M"}, {"C"}, {"T"}]
    food_num = [0, 0, 0, 0, 0, 0, 0]
    for r in range(n):
        for c in range(n):
            for x, food in enumerate(foods):
                if grid[r][c] == food:
                    food_num[x] += power[r][c]
                    break

    return food_num


#########################################################
#########################################################
#########################################################
day = 0
while day < t:
    breakfast()
    leaders = lunch()
    dinner(leaders)

    ans = get_sum()
    for elem in ans:
        print(elem, end=" ")
    print()
    day += 1