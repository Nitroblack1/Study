# 루돌프의 반란 — 정답 풀이 (Python3)

import sys
input = sys.stdin.readline

n, m, p, c, d = map(int, input().split())
r = list(map(int, input().split()))  # 루돌프 위치 (1-index)

# 산타 상태
pos = [(-1, -1)] * (p + 1)       # 각 산타 id -> (x, y), 격자 밖이면 (-1, -1)
grid = [[0] * (n + 1) for _ in range(n + 1)]  # 1..n 사용, 0은 빈칸
for _ in range(p):
    i, x, y = map(int, input().split())
    pos[i] = (x, y)
    grid[x][y] = i

score = [0] * (p + 1)
alive = [False] + [True] * p
stun_until = [0] * (p + 1)  # t턴에 기절하면 t와 t+1 두 턴 동안 못 움직임(포함)

def inb(x, y):
    return 1 <= x <= n and 1 <= y <= n

def sqdist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def pick_target():
    """루돌프가 노릴 산타 id 선택 (가까운->행 큰->열 큰)"""
    best, best_d = None, 10**18
    for i in range(1, p + 1):
        if not alive[i]:
            continue
        d2 = sqdist(r, pos[i])
        if d2 < best_d:
            best_d, best = d2, i
        elif d2 == best_d:
            x, y = pos[i]
            bx, by = pos[best]
            if (x, y) > (bx, by):
                best = i
    return best

def chain_push(sid, dx, dy):
    """체인 상호작용: 목표 칸에 산타가 있으면 그 산타를 같은 방향으로 1칸 밀어내기 (재귀)"""
    sx, sy = pos[sid]
    nx, ny = sx + dx, sy + dy
    if not inb(nx, ny):
        # 격자 밖으로 밀리면 탈락
        grid[sx][sy] = 0
        pos[sid] = (-1, -1)
        alive[sid] = False
        return
    nxt = grid[nx][ny]
    if nxt != 0:
        chain_push(nxt, dx, dy)  # 먼저 앞사람부터 밀어 비우기(또는 탈락)
    if grid[nx][ny] != 0:
        # 이 경우는 거의 없지만, 안전장치
        return
    grid[sx][sy] = 0
    grid[nx][ny] = sid
    pos[sid] = (nx, ny)

def apply_push(sid, dx, dy, power):
    """산타 sid를 (dx,dy) 방향으로 power칸 '날리기'.
       착지 칸이 차 있으면 chain_push로 1칸씩 연쇄 밀치기."""
    sx, sy = pos[sid]
    tx, ty = sx + dx * power, sy + dy * power
    if not inb(tx, ty):
        grid[sx][sy] = 0
        pos[sid] = (-1, -1)
        alive[sid] = False
        return
    occ = grid[tx][ty]
    if occ != 0:
        chain_push(occ, dx, dy)
    grid[sx][sy] = 0
    grid[tx][ty] = sid
    pos[sid] = (tx, ty)

# 4방(산타 이동 우선순위): 상, 우, 하, 좌
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

t = 1
while t <= m and any(alive[1:]):
    # ── 루돌프 턴 ──
    tgt = pick_target()
    tx, ty = pos[tgt]
    # 루돌프 한 칸 이동 (목표 산타를 향해 대각 포함)
    dx = 0 if tx == r[0] else (1 if tx > r[0] else -1)
    dy = 0 if ty == r[1] else (1 if ty > r[1] else -1)
    r[0] += dx
    r[1] += dy

    # 루돌프와 충돌
    sid = grid[r[0]][r[1]]
    if sid != 0:
        score[sid] += c
        stun_until[sid] = t + 1
        apply_push(sid, dx, dy, c)

    # ── 산타 턴 ── (id 오름차순)
    for i in range(1, p + 1):
        if not alive[i]:
            continue
        if t <= stun_until[i]:
            continue  # 기절 중
        sx, sy = pos[i]
        base_d = sqdist(r, (sx, sy))
        best_pos = None
        best_d = base_d
        chosen_dir = None
        for (dx, dy) in dirs:
            nx, ny = sx + dx, sy + dy
            if not inb(nx, ny) or grid[nx][ny] != 0:
                continue
            nd = sqdist(r, (nx, ny))
            if nd < best_d:
                best_d = nd
                best_pos = (nx, ny)
                chosen_dir = (dx, dy)
        if best_pos is None:
            continue  # 못 움직임

        # 이동
        grid[sx][sy] = 0
        nx, ny = best_pos

        # 루돌프와 충돌 시: 점수 D, 반대방향으로 D칸 밀려남 + 기절
        if nx == r[0] and ny == r[1]:
            score[i] += d
            stun_until[i] = t + 1
            pos[i] = (nx, ny)                # 충돌 지점에 위치한 뒤
            bdx, bdy = -chosen_dir[0], -chosen_dir[1]
            apply_push(i, bdx, bdy, d)       # 반대 방향으로 D칸
        else:
            grid[nx][ny] = i
            pos[i] = (nx, ny)

    # ── 턴 종료: 생존 산타 +1점 ──
    for i in range(1, p + 1):
        if alive[i]:
            score[i] += 1

    t += 1

print(*score[1:])
