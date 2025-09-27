from collections import deque

n, m = map(int, input().split())
m_temp = list(map(int, input().split()))
w_temp = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]

medusa = (m_temp[0], m_temp[1])
park = (m_temp[2], m_temp[3])
warriors = []
for a in range(m):
    warriors.append(w_temp[a*2:a*2+2] + [False])

# 상, 하, 좌, 우
dis, djs = [-1, 1, 0, 0], [0, 0, -1, 1]
############################################################
def debug(board):
    for r in board:
        for c in r:
            print(int(c), end=" ")
        print()
    print()


def inb(i, j):
    return 0 <= i < n and 0 <= j < n


def find_bfs():
    from_where = [
        [(-1, -1) for _ in range(n)]
        for _ in range(n)
    ]
    q = deque()

    from_where[medusa[0]][medusa[1]] = (medusa[0], medusa[1])
    q.append(tuple(medusa))
    found = False
    while q and not found:
        ci, cj = q.popleft()
        for di, dj in zip(dis, djs):
            ni, nj = ci + di, cj + dj
            if inb(ni, nj) and from_where[ni][nj] == (-1, -1) and grid[ni][nj] == 0:
                if ni == park[0] and nj == park[1]:
                    from_where[ni][nj] = (ci, cj)
                    found = True
                    break
                from_where[ni][nj] = (ci, cj)
                q.append((ni, nj))

    # 경로가 없다면
    if not found:
        return -1

    path = [(park[0], park[1])]
    ci, cj = park[0], park[1]
    while ci != medusa[0] or cj != medusa[1]:
        path.append(from_where[ci][cj])
        ci, cj = from_where[ci][cj]

    path.pop()
    return path


def m_move(m_path):
    global medusa, warriors
    if m_path:
        cnt = 0
        medusa = m_path.pop()
        for w in warriors:
            if medusa[0] == w[0] and medusa[1] == w[1]:
                w[0], w[1] = -1, -1
                cnt += 1

        # 죽인 w가 있으면
        if cnt > 0:
            if cnt == len(warriors):
                warriors = []
            else:
                warriors.sort(key=lambda x: x[0])
                warriors = warriors[cnt:]


def get_sight(i, vision_temp):
    # 상
    if i == 0:
        for c in range(medusa[1] - 1, -1, -1):
            for r in range(0, medusa[0] - (medusa[1] - c) + 1):
                vision_temp[r][c] = True
        for r in range(0, medusa[0]):
            vision_temp[r][medusa[1]] = True
        for c in range(medusa[1] + 1, n):
            for r in range(medusa[0] + medusa[1] - c + 1):
                vision_temp[r][c] = True

    # 하
    elif i == 1:
        for c in range(medusa[1]):
            for r in range(medusa[0] + (medusa[1] - c), n):
                vision_temp[r][c] = True
        for r in range(medusa[0] + 1, n):
            vision_temp[r][medusa[1]] = True
        for c in range(medusa[1] + 1, n):
            for r in range(medusa[0] - (medusa[1] - c), n):
                vision_temp[r][c] = True

    # 좌
    elif i == 2:
        for r in range(medusa[0] - 1, -1, -1):
            for c in range(medusa[1] - (medusa[0] - r) + 1):
                vision_temp[r][c] = True
        for c in range(medusa[1] - 1, -1, -1):
            vision_temp[medusa[0]][c] = True
        for r in range(medusa[0] + 1, n):
            for c in range(medusa[1] + (medusa[0] - r) + 1):
                vision_temp[r][c] = True

    # 우
    elif i == 3:
        for r in range(medusa[0] - 1, -1, -1):
            for c in range(medusa[1] + (medusa[0] - r), n):
                vision_temp[r][c] = True
        for c in range(medusa[1] + 1, n):
            vision_temp[medusa[0]][c] = True
        for r in range(medusa[0] + 1, n):
            for c in range(medusa[1] + (r - medusa[0]), n):
                vision_temp[r][c] = True


def cover(wr, wc, vision_temp):
    """
    vision_temp[r][c] 가 True인 칸 = 시야에 보이는 칸.
    전사 (wr, wc)를 '경계'로 하여, 전사 '뒤쪽'을 같은 갈래(좌/중앙/우)로만 BFS 확장하며 False로 지움.
    dir_idx 없이 메두사-전사 상대 위치로 현재 시야 쐐기(상/하/좌/우)와 갈래를 내부에서 판정.
    """
    mr, mc = medusa
    dr, dc = wr - mr, wc - mc   # 전사 - 메두사 상대 좌표

    # 1) 현재 시야 쐐기(상/하/좌/우)와 그에 대응하는 3갈래 방향벡터(dxys3) 결정
    #    - 세로 쐐기: |dr| >= |dc|  (상/하)
    #    - 가로 쐐기: |dr| <  |dc|  (좌/우)
    if abs(dr) >= abs(dc):
        # 세로 쐐기
        if dr < 0:
            # 상
            dxys3 = [(-1, -1), (-1,  0), (-1,  1)]  # 좌대각, 중앙, 우대각
            # 2) 갈래 t 결정 (0=좌대각, 1=중앙, 2=우대각)
            t = 1 if dc == 0 else (0 if dc < 0 else 2)
        else:
            # 하
            dxys3 = [( 1, -1), ( 1,  0), ( 1,  1)]
            t = 1 if dc == 0 else (0 if dc < 0 else 2)
    else:
        # 가로 쐐기
        if dc < 0:
            # 좌
            dxys3 = [(-1, -1), ( 0, -1), ( 1, -1)]
            t = 1 if dr == 0 else (0 if dr < 0 else 2)  # 위=좌갈래(0), 같은 행=중앙(1), 아래=우갈래(2)
        else:
            # 우
            dxys3 = [(-1,  1), ( 0,  1), ( 1,  1)]
            t = 1 if dr == 0 else (0 if dr < 0 else 2)

    # 3) 전사 뒤쪽 지우기 BFS
    #    - 전사 칸은 그대로 두고, 같은 갈래로만 퍼지며 vision_temp를 False로 만든다.
    q = deque()
    q.append((wr, wc))
    while q:
        x, y = q.popleft()
        for d, (dxi, dyi) in enumerate(dxys3):
            # 갈래 제한: 중앙이면 중앙만, 좌갈래면 좌/중, 우갈래면 우/중
            if t == 1 and d != 1:
                continue
            if t == 0 and d == 2:
                continue
            if t == 2 and d == 0:
                continue
            nx, ny = x + dxi, y + dyi
            if not inb(nx, ny):
                continue
            if vision_temp[nx][ny]:          # 보이는 칸만 지움
                vision_temp[nx][ny] = False
                q.append((nx, ny))



def m_sight():
    max_stone_num = 0
    max_stoned_w = []
    vision = [
        [False for _ in range(n)]
        for _ in range(n)
    ]

    # stone이 가장 많은 방향 찾기 [상, 하, 좌, 우]
    for i in range(4):
        vision_temp = [
            [False for _ in range(n)]
            for _ in range(n)
        ]
        get_sight(i, vision_temp)
        stoned_w = []

        # 정렬 debug 필요
        warriors.sort(key=lambda x: (abs(x[0] - medusa[0]), abs(x[1] - medusa[1])))
        for idx, w in enumerate(warriors):
            if vision_temp[w[0]][w[1]]:
                cover(w[0], w[1], vision_temp)
                stoned_w.append(idx)


        # 만약 최대 비전을 찾았다면, max & vision 갱신
        if len(stoned_w) > max_stone_num:
            max_stone_num = len(stoned_w)
            vision = [row[:] for row in vision_temp]
            max_stoned_w = stoned_w


    for idx in max_stoned_w:
        warriors[idx][2] = True

    return max_stone_num, vision


def w_move(vision):
    moved_len = 0
    for w in warriors:
        # if not stone
        if not w[2]:
            # first move
            for di, dj in zip(dis, djs):
                ni, nj = w[0] + di, w[1] + dj
                c_dis = abs(medusa[0] - w[0]) + abs(medusa[1] - w[1])
                n_dis = abs(medusa[0] - ni) + abs(medusa[1] - nj)
                # 격자 안 && 거리를 줄일 수 있다면 && 메두사 시야각 밖이라면
                if inb(ni, nj) and n_dis < c_dis and not vision[ni][nj]:
                    w[0], w[1] = ni, nj
                    moved_len += 1
                    break

            # 첫 번째 움직임만에 메두사에 닿으면
            if w[0] == medusa[0] and w[1] == medusa[1]:
                break

            # 좌, 우, 상, 하
            sec_move = [[0, -1], [0, 1], [-1, 0], [1, 0]]
            for ds in sec_move:
                ni, nj = w[0] + ds[0], w[1] + ds[1]
                c_dis = abs(medusa[0] - w[0]) + abs(medusa[1] - w[1])
                n_dis = abs(medusa[0] - ni) + abs(medusa[1] - nj)
                # 격자 안 && 거리를 줄일 수 있다면 && 메두사 시야각 박이라면
                if inb(ni, nj) and n_dis < c_dis and not vision[ni][nj]:
                    w[0], w[1] = ni, nj
                    moved_len += 1
                    break
        else:
            w[2] = False
    return moved_len


def w_attack():
    global warriors
    atk_cnt = 0
    for w in warriors:
        if w[0] == medusa[0] and w[1] == medusa[1]:
            w[0], w[1] = -1, -1
            atk_cnt += 1

    # 만약 공격했다면
    if atk_cnt > 0:
        if atk_cnt == len(warriors):
            warriors = []
        else:
            warriors.sort(key=lambda x: x[0])
            warriors = warriors[atk_cnt:]
    return atk_cnt


def simulate():
    # Sr, Sc 다음 칸부터 공원까지 경로
    m_path = find_bfs()
    if m_path == -1:
        print(-1)
        return
    while medusa != park:
        m_move(m_path)
        if medusa == park:
            break
        stone_num, vision = m_sight()
        path_len = w_move(vision)
        attack_num = w_attack()

        print(path_len, stone_num, attack_num)

    print(0)

############################################################
############################################################
############################################################
simulate()