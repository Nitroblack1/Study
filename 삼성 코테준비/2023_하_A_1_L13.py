from collections import deque

l, n, q = map(int, input().split())
# 0: 빈칸 / 1: 함정 / 2: 벽
grid = [list(map(int, input().split())) for _ in range(l)]
# r, c, h, w, k
knights = [list(map(int, input().split())) for _ in range(n)]
# i, d -> i번째 기사에게 d 방향으로 1칸 이동 지시
orders = [list(map(int, input().split())) for _ in range(q)]
# 초기 HP를 저장해서 생존한 기사들의 대미지 합 구하는 용도
init_hp = []
# 기사들 현재 영역 좌표
k_areas = []
# 기사들 현재 영역맵
k_map = [
    [0 for _ in range(l)]
    for _ in range(l)
]

for i, knight in enumerate(knights, 1):
    temp = []
    init_hp.append(knight[4])
    for height in range(knight[2]):
        for width in range(knight[3]):
            temp.append([height + knight[0] - 1, width + knight[1] - 1])
            k_map[height + knight[0] - 1][width + knight[1] - 1] = i
    k_areas.append(temp)

def debug(matrix):
    for r in matrix:
        for c in r:
            print(c, end=" ")
        print()
    print()

######### CAUTION #########
# orders의 i는 index + 1
# k_map 상에서 r, c는 0행, 0열부터 index 시작.
######### CAUTION #########


####### Common def ########
def inbound(r, c):
    if 0 <= r < l and 0 <= c < l:
        return True
    return False

def can_go(r, c):
    if grid[r][c] == 2:
        return False
    return True

direction = {
    0: [-1, 0],
    1: [0, 1],
    2: [1, 0],
    3: [0, -1]
}
####### Common def ########



def simulate():
    turn = 0
    while turn < q:
        if knights[orders[turn][0] - 1][4] == 0:
            continue
        if move(orders[turn]):
            turn += 1
            # combat()
        turn += 1


def move(order):
    finished = False
    ds = direction.get(order[1])
    que = deque()
    que.append(order[0])
    total_area = []

    while que:
        temp_area = []
        std = que.pop()
        cur_k_area = k_areas[std - 1]

        for area in cur_k_area:
            nr, nc = area[0] + ds[0], area[1] + ds[1]
            if inbound(nr, nc) and can_go(nr, nc):
                temp_area.append([nr, nc])
                if k_map[nr][nc] != 0 and k_map[nr][nc] != std:
                    que.append(k_map[nr][nc])
            else:
                return
        total_area.append([std, temp_area])

    # 어떻게 흔적을 지울 것인가?
    print(order)
    print('before')
    debug(k_map)
    for area in total_area:
        k_areas[area[0] - 1] = area[1][:]
        for indices in area[1]:
            k_map[indices[0]][indices[1]] = area[0]


    print('after')
    debug(k_map)
    print(total_area)


#############################################
print(simulate())