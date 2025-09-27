# 방향 벡터 (상, 우, 하, 좌)
dis = [-1, 0, 1, 0]
djs = [0, 1, 0, -1]


# 1차원상에서 두 구간 [a, b]와 [c, d]가 겹치는지 판정하는 함수
def is_overlapped(a: int, b: int, c: int, d: int) -> bool:
    assert a <= b and c <= d, "Invalid arguments"
    # 겹치지 않는 경우를 제외하면 겹치는 경우임
    return not (b < c or d < a)


class Knight:
    """
    각 기사의 정보를 담는 클래스.
    위치, 크기, 체력, 누적 대미지 등의 상태와 관련 연산을 메서드로 관리합니다.
    """

    def __init__(self, i: int, j: int, h: int, w: int, power: int) -> None:
        self.si: int = i  # 좌상단 행
        self.sj: int = j  # 좌상단 열
        self.h: int = h  # 높이
        self.w: int = w  # 너비
        self.power: int = power  # 초기 체력
        self.total_damage: int = 0  # 누적 데미지

    @property
    def ei(self) -> int:
        # 우하단 행 좌표
        return self.si + self.h - 1

    @property
    def ej(self) -> int:
        # 우하단 열 좌표
        return self.sj + self.w - 1

    def is_alive(self) -> bool:
        # 기사의 생존 여부 확인
        return self.power > 0

    def is_pushed(self, other: "Knight", direction: int) -> bool:
        """
        'other' 기사가 'direction'으로 이동했을 때, 현재 기사('self')와 겹치는지 확인.
        즉, 현재 기사가 밀려나는지 여부를 판정합니다.
        """
        global dis, djs

        # other 기사가 이동한 후의 위치와 현재 기사의 위치가 겹치는지 확인
        return (
                is_overlapped(
                    a=self.si, b=self.ei,
                    c=other.si + dis[direction], d=other.ei + dis[direction],
                ) and
                is_overlapped(
                    a=self.sj, b=self.ej,
                    c=other.sj + djs[direction], d=other.ej + djs[direction],
                )
        )

    def can_move(self, direction: int) -> bool:
        """
        주어진 방향으로 이동 시 체스판을 벗어나거나 벽과 부딪히는지 확인.
        누적합 배열(sum_walls)을 이용하여 O(1)에 벽 존재 여부를 판별합니다.
        """
        global dis, djs, l, sum_walls

        # 이동 후의 예상 좌표
        moved_si: int = self.si + dis[direction]
        moved_ei: int = self.ei + dis[direction]
        moved_sj: int = self.sj + djs[direction]
        moved_ej: int = self.ej + djs[direction]

        # 체스판 경계를 벗어나는지 확인
        if not (
                1 <= moved_si and moved_ei <= l and
                1 <= moved_sj and moved_ej <= l
        ):
            return False

        # 이동할 위치에 벽이 있는지 누적합을 이용해 확인
        if 0 < (
                sum_walls[moved_ei][moved_ej]
                - sum_walls[moved_ei][moved_sj - 1]
                + sum_walls[moved_si - 1][moved_sj - 1]
                - sum_walls[moved_si - 1][moved_ej]
        ):
            return False

        return True

    def move(self, direction: int) -> None:
        """기사의 위치를 실제로 이동시킵니다."""
        global dis, djs

        self.si += dis[direction]
        self.sj += djs[direction]

    def get_damage(self) -> int:
        """
        기사가 현재 위치한 영역의 함정 수를 누적합 배열(sum_traps)을 이용해 계산.
        """
        global sum_traps

        return (
                sum_traps[self.ei][self.ej]
                - sum_traps[self.ei][self.sj - 1]
                + sum_traps[self.si - 1][self.sj - 1]
                - sum_traps[self.si - 1][self.ej]
        )

    def desc_power(self, damage: int) -> None:
        """
        계산된 대미지를 체력에 반영하고, 누적 대미지를 기록합니다.
        실제 깎이는 체력은 현재 체력을 초과할 수 없습니다.
        """
        damage = max(0, min(self.power, damage))
        self.power -= damage
        self.total_damage += damage


# 전역 변수 선언
l: int = 0
n: int = 0
q: int = 0

board: list[list[int]] = []
sum_traps: list[list[int]] = []  # 함정 누적합 배열
sum_walls: list[list[int]] = []  # 벽 누적합 배열

knights: list[Knight] = []

visited: list[bool] = []  # 연쇄 이동 판별 시 방문 여부 체크


def dfs_knight(idx: int, direction: int) -> bool:
    """
    idx번 기사부터 시작되는 연쇄 이동이 가능한지 재귀적으로 탐색(DFS).
    하나라도 벽에 막히면 연쇄 이동은 불가능합니다.
    """
    global visited, knights, n

    # 현재 연쇄 이동 탐색에서 이미 확인한 기사는 패스
    visited[idx] = True

    # 현재 기사가 벽에 막히는지 확인 (재귀의 기저 사례)
    if not knights[idx].can_move(direction=direction):
        return False

    # 현재 기사로 인해 밀려나는 다른 기사들을 찾아 재귀적으로 탐색
    for next_idx in range(n):
        if (
                not visited[next_idx] and
                knights[next_idx].is_alive() and
                knights[next_idx].is_pushed(other=knights[idx], direction=direction)
        ):
            # 연쇄적으로 밀리는 다음 기사도 이동 가능한지 확인
            if not dfs_knight(idx=next_idx, direction=direction):
                return False

    # 모든 연쇄 이동이 가능한 경우
    return True


def move_knight(start_idx: int, direction: int) -> None:
    """하나의 명령을 처리하는 메인 함수."""
    global knights, visited, n

    # 사라진 기사에게 명령을 내린 경우 무시
    if not knights[start_idx].is_alive():
        return

    # 1. 연쇄 이동 가능성 판별
    visited = [False] * n
    if not dfs_knight(idx=start_idx, direction=direction):
        return

    # 2. 실제 이동 및 대미지 계산
    for idx in range(n):
        # 연쇄 이동에 포함된 기사들만 처리
        if visited[idx]:
            knights[idx].move(direction=direction)
            # 명령을 직접 받은 기사는 대미지를 입지 않음
            if idx != start_idx:
                damage: int = knights[idx].get_damage()
                knights[idx].desc_power(damage=damage)


def process_init() -> None:
    """입력을 받고 게임에 필요한 초기 설정을 수행합니다."""
    global l, n, q, board, sum_traps, sum_walls, knights

    l, n, q = map(int, input().split())
    board = [[0] * (l + 1) for _ in range(l + 1)]

    for i in range(1, l + 1):
        line = list(map(int, input().split()))
        for j in range(1, l + 1):
            board[i][j] = line[j - 1]

    # 2차원 누적합 배열 계산 (함정)
    sum_traps = [[0] * (l + 1) for _ in range(l + 1)]
    for i in range(1, l + 1):
        for j in range(1, l + 1):
            sum_traps[i][j] = (
                    sum_traps[i][j - 1]
                    - sum_traps[i - 1][j - 1]
                    + sum_traps[i - 1][j]
                    + (1 if 1 == board[i][j] else 0)
            )

    # 2차원 누적합 배열 계산 (벽)
    sum_walls = [[0] * (l + 1) for _ in range(l + 1)]
    for i in range(1, l + 1):
        for j in range(1, l + 1):
            sum_walls[i][j] = (
                    sum_walls[i][j - 1]
                    - sum_walls[i - 1][j - 1]
                    + sum_walls[i - 1][j]
                    + (1 if 2 == board[i][j] else 0)
            )

    # 기사 정보 초기화
    for _ in range(n):
        i, j, h, w, k = map(int, input().split())
        knights.append(Knight(i=i, j=j, h=h, w=w, power=k))


# --- 메인 실행 로직 ---
process_init()

# Q개의 명령을 순차적으로 처리
for _ in range(q):
    i, d = map(int, input().split())
    move_knight(start_idx=i - 1, direction=d)  # 기사 번호는 1-based, 인덱스는 0-based

# 최종 결과 계산
answer: int = 0
for idx in range(n):
    # 살아있는 기사들의 누적 대미지를 합산
    if knights[idx].is_alive():
        answer += knights[idx].total_damage

print(answer)
