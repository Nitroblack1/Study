from collections import deque

n, m, k = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
attacked_order = [[0] * m for _ in range(n)]

def main():
    turn = 1
    alive = m
    while turn <= k and alive > 1:
        # 공격자 선정 후
        cur_atk = select_attacker()

        power = field[cur_atk[0]][cur_atk[1]] + m + n
        # 공격 대상자 선정
        cur_tgt = select_target()

        # 공격력 보강한다.
        field[cur_atk[0]][cur_atk[1]] += m + n

        # 레이저 or 포탄, 좌표 정보만 전달
        attack_list = find_method(cur_atk[:2], cur_tgt[:2])
        attack(attack_list, cur_atk, cur_tgt, power)

        # 포탑 정보 업데이트
        alive = update(attack_list, cur_tgt, cur_atk)

        # 공격 턴 업데이트
        attacked_order[cur_atk[0]][cur_atk[1]] = turn
        turn += 1


def select_attacker():
    # 1. 공격력이 가장 낮은 포탑들
    min_attack = 5000
    weakest_turrets = []
    for r in range(n):
        for c in range(m):
            if field[r][c] == 0:
                continue
            # 만약 새로운 최저점을 찾으면 그 값으로 설정하고, 기존 배열 초기화
            if field[r][c] < min_attack:
                min_attack = field[r][c]
                weakest_turrets = []
            # 최저점과 같으면 추가
            if field[r][c] == min_attack:
                # 해당 터렛 좌표와 공격 이력 추가
                weakest_turrets.append([r, c, attacked_order[r][c]])
    if len(weakest_turrets) == 1:
        return weakest_turrets[0]

    # 2. 가장 최근에 공격한 포탑 선정
    weakest_turrets.sort(key=lambda x: [-x[2]])
    latest_turn = weakest_turrets[0][2]
    for i, turrets in enumerate(weakest_turrets):
        if turrets[2] < latest_turn:
            weakest_turrets = weakest_turrets[:i]
            break
    if len(weakest_turrets) == 1:
        return weakest_turrets[0]

    # 3. 행과 열의 합이 가장 큰 포탑.
    weakest_turrets.sort(key=lambda x: [- (x[0] + x[1])])
    largest_rc_sum = weakest_turrets[0][0] + weakest_turrets[0][1]
    for i, turrets in enumerate(weakest_turrets):
        if turrets[0] + turrets[1] < largest_rc_sum:
            weakest_turrets = weakest_turrets[:i]
            break
    if len(weakest_turrets) == 1:
        return weakest_turrets[0]

    # 4. 열 값이 가장 큰 포탑. ### check 하진 않음.
    weakest_turrets.sort(key=lambda x: [-x[1]])
    return weakest_turrets[0]


def select_target():
    # 1. 공격력이 가장 높은 포탑
    max_attack = 0
    strongest_turrets = []
    for r in range(n):
        for c in range(m):
            if field[r][c] == 0:
                continue
            # 만약 새로운 최고점을 찾으면 그 값으로 설정하고, 기존 배열 초기화
            if field[r][c] > max_attack:
                max_attack = field[r][c]
                strongest_turrets = []
            # 최고점과 같으면 추가
            if field[r][c] == max_attack:
                # 해당 터렛 좌표와 공격 이력 추가
                strongest_turrets.append([r, c, attacked_order[r][c]])
    if len(strongest_turrets) == 1:
        return strongest_turrets[0]

    # 2. 공격한지 가장 오래된 포탑
    strongest_turrets.sort(key=lambda x: [x[2]])
    oldest_turn = strongest_turrets[0][2]
    for i, turrets in enumerate(strongest_turrets):
        if turrets[2] > oldest_turn:
            strongest_turrets = strongest_turrets[:i]
            break
    if len(strongest_turrets) == 1:
        return strongest_turrets[0]

    # 3. 행과 열의 합지 가장 작은 포탑
    strongest_turrets.sort(key=lambda x: [x[0] + x[1]]) # 체크 필요
    smallest_rc_sum = strongest_turrets[0][0] + strongest_turrets[0][1]
    for i, turrets in enumerate(strongest_turrets):
        if turrets[0] + turrets[1] > smallest_rc_sum:
            strongest_turrets = strongest_turrets[:i]
            break
    if len(strongest_turrets) == 1:
        return strongest_turrets[0]

    # 4. 열 값이 가장 작은 포탑. ### check 하진 않음.
    strongest_turrets.sort(key=lambda x: [x[1]])
    return strongest_turrets[0]


def find_method(start, end):
    q = deque()
    # 우 / 하 / 좌 / 상
    dis, djs = [0, 1, 0, -1], [1, 0, -1, 0]
    visited = [[False] * m for _ in range(n)]
    q.append((start[0], start[1]))
    visited[start[0]][start[1]] = True
    from_where = [
        [(-1, -1) for _ in range(m)]
        for _ in range(n)
    ]

    from_where[start[0]][start[1]] = (start[0], start[1])

    while q:
        ci, cj = q.popleft()
        for di, dj in zip(dis, djs):
            # next idx 조정
            ni, nj = (ci + di) % n, (cj + dj) % m
            # 만약 부서진 포탑이거나 방문한 곳이 아니면 간다.
            if from_where[ni][nj] == (-1, -1) and not field[ni][nj] == 0:
                q.append((ni, nj))
                from_where[ni][nj] = (ci, cj)

    path = []
    if from_where[end[0]][end[1]] != (-1, -1):
        cur_i, cur_j = end[0], end[1]
        while (cur_i, cur_j) != (start[0], start[1]):
            if (cur_i, cur_j) != (end[0], end[1]):
                path.append((cur_i, cur_j))
            cur_i, cur_j = from_where[cur_i][cur_j]
        return path

    # 만약 레이저 공격이 안되면, 포탄 공격
    drs, dcs = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
    for dr, dc in zip(drs, dcs):
        nr, nc = (end[0] + dr) % n, (end[1] + dc) % m
        path.append((nr, nc))

    return path

def inb(r, c):
    if 0 <= r < n and 0 <= c < m:
        return True
    return False


def attack(at_list, att, tgt, power):
    for atk in at_list:
        if att[0] == atk[0] and att[1] == atk[1]:
            continue
        field[atk[0]][atk[1]] -= (power // 2)

    field[tgt[0]][tgt[1]] -= power
    return

def update(at_list, tgt, atk):
    alive = 0
    for i in range(n):
        for j in range(m):
            is_attacked = False
            if field[i][j] == 0:
                continue
            if field[i][j] < 0:
                field[i][j] = 0
                continue

            if field[i][j] != 0:
                alive += 1

            if (tgt[0] == i and tgt[1] == j) or (atk[0] == i and atk[1] == j):
                continue
            for at in at_list:
                if at == (i, j):
                    is_attacked = True
                    break

            if not is_attacked:
                field[i][j] += 1

    return alive


main()
answer_t = select_target()
print(field[answer_t[0]][answer_t[1]])