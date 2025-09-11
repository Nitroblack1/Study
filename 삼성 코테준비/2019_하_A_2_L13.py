# W, R, B
# 1 ~ k번째 말까지 순서대로 움직임.
# 아직 한 턴이 다 끝나지 않아도 말이 4개 이상 겹치면 즉시 게임 종료
from collections import deque
n, k = map(int, input().split())
# 0 : w / 1 : r / 2 : b
area_map = [list(map(int, input().split())) for _ in range(n)]

horses_map = [[[] for _ in range(n)] for _ in range(n)]
horses = []
R, L, U, D = 1, 2, 3, 4
for num in range(k):
    # x, y, d | d : 1 - R / 2 - L / 3 - U / 4 - D
    # index 전부 0으로 맞췄음.
    x, y, d = list(map(int, input().split()))
    horses_map[x-1][y-1].append(num)
    horses.append([num, x - 1, y - 1, d])

turn = 0
def game():
    global turn
    while turn < 1000:
        turn += 1
        for horse in horses:
            # 조건에 맞춰서 말을 이동한다.
            if get_next_pos(horse):
                return


def is_game_over(i, j):
    if len(horses_map[i][j]) >= 4:
        return True
    return False

def get_next_pos(h):
    ds, cx, cy = [0, 0], h[1], h[2]
    if h[3] == R:
        ds = [0, 1]
    if h[3] == L:
        ds = [0, -1]
    if h[3] == U:
        ds = [-1, 0]
    if h[3] == D:
        ds = [1, 0]

    # 다음 칸 후보 계산
    new_x, new_y, new_d = cx + ds[0], cy + ds[1], h[3]

    # 만약 이동하려는 곳이 범위 바깥 or 파란 칸이면
    if not is_inbound(new_x, new_y) or area_map[new_x][new_y] == 2:
        # 일단 방향은 바꿔야 한다.
        new_x, new_y, h[3] = cx - ds[0], cy - ds[1], turn_around(h[3])
        # 그 뒤에도 파란 칸 or 범위 바깥이라면
        if not is_inbound(new_x, new_y) or area_map[new_x][new_y] == 2:
            # 그대로 둔다.
            return False

    # 만약 빨간 칸이면
    if area_map[new_x][new_y] == 1:
        # 보드 상태 업데이트
        for s in range(len(horses_map[cx][cy])):
            # 이동하는 말부터
            if horses_map[cx][cy][s] == h[0]:
                # 얹힌 순서를 역전하여 이동한다.
                horses_map[new_x][new_y] += horses_map[cx][cy][s:][::-1]
                horses_map[cx][cy] = horses_map[cx][cy][:s]
                break


        # 말 위치 정보 업데이트
        for horse in horses:
            for moved_horse in horses_map[new_x][new_y]:
                if moved_horse == horse[0]:
                    horse[1], horse[2] = new_x, new_y

        if is_game_over(new_x, new_y):
            return True
        return False


    # 만약 일반 칸이면
    if area_map[new_x][new_y] == 0:
        # 보드 상태 업데이트
        for s in range(len(horses_map[cx][cy])):
            # 이동하는 말부터
            if horses_map[cx][cy][s] == h[0]:
                horses_map[new_x][new_y] += horses_map[cx][cy][s:]
                horses_map[cx][cy] = horses_map[cx][cy][:s]
                break

        # 말 위치 정보 업데이트
        for horse in horses:
            for moved_horse in horses_map[new_x][new_y]:
                if moved_horse == horse[0]:
                    horse[1], horse[2] = new_x, new_y

        if is_game_over(new_x, new_y):
            return True
        return False

def turn_around(direction):
    if direction == U:
        return D
    if direction == D:
        return U
    if direction == L:
        return R
    if direction == R:
        return L

def is_inbound(i, j):
    if 0 <= i < n and 0 <= j < n:
        return True
    return False

########## Main ##########
game()
if turn >= 1000:
    print(-1)
else:
    print(turn)
