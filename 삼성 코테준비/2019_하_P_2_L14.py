moves = list(map(int, input().split()))

# 각 경로 정보 설정
m = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]  # 21
sc_10 = [0, 0, 0, 0, 0, 0, 13, 16, 19, 25, 30, 35, 40]                                # 13
sc_20 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 24, 25, 30, 35, 40]                     # 17
sc_30 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 27, 26, 25, 30, 35, 40]  # 23
paths = [m, sc_10, sc_20, sc_30]

# 같은 물리 칸은 같은 ID로 매핑 (겹침 판정용)
id_m     = list(range(21))  # 메인 0..20
id_sc_10 = [0,1,2,3,4,5, 21,22,23, 24,25,26, 20]                 # 10(=메인5)은 ID 5, 25/30/35/40 합류 ID 24/25/26/20
id_sc_20 = [0,1,2,3,4,5,6,7,8,9,10, 27,28, 24,25,26, 20]         # 20(=메인10)은 ID 10
id_sc_30 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 29,30,31, 24,25,26, 20]
id_paths = [id_m, id_sc_10, id_sc_20, id_sc_30]

case = []
max_score = 0

def cases(cnt):
    global max_score
    if cnt == 9:  # 첫 수는 1번 말로 고정, 이후 9번만 선택
        max_score = max(max_score, get_score())
        return
    for i in range(1, 5):
        case.append(i)
        cases(cnt + 1)
        case.pop()

def get_score():
    # 4개의 말 (1~4번), [pos, path]  / path: 0=메인, 1/2/3=분기, -1=도착
    if moves[0] == 5:
        # 첫 수가 5면 메인 10 착지 후 다음부터 분기(1) 진행
        horses = [[0, 0], [moves[0], 1], [0, 0], [0, 0], [0, 0]]
    else:
        horses = [[0, 0], [moves[0], 0], [0, 0], [0, 0], [0, 0]]

    score = paths[0][moves[0]]  # 첫 착지 점수는 메인 기준으로 더함
    i = 1  # 다음 주사위 인덱스

    for h in case:
        # 도착한 말은 못 움직임
        if horses[h][1] == -1:
            return -1

        cur_path = horses[h][1]
        cur_pos  = horses[h][0]
        next_pos = cur_pos + moves[i]

        # 도착선을 넘으면 도착 처리 (주사위는 소비)
        if next_pos >= len(paths[cur_path]):
            horses[h][1] = -1
            i += 1
            continue

        # 분기: 기본은 현재 경로 유지! (메인에서 5/10/15에 '착지'하면 분기로 전환)
        next_path = cur_path
        if cur_path == 0:
            if next_pos == 5:
                next_path = 1
            elif next_pos == 10:
                next_path = 2
            elif next_pos == 15:
                next_path = 3

        # 겹침 판정: 같은 '칸 ID'면 불가 (도착한 말은 제외)
        target_id = id_paths[next_path][next_pos]
        for p in range(1, 5):
            if p == h:
                continue
            if horses[p][1] == -1:
                continue
            other_id = id_paths[horses[p][1]][horses[p][0]]
            if target_id == other_id:
                return -1

        # 점수는 '현재 경로' 기준으로 해당 칸 값 더함 (분기는 다음 이동부터 반영)
        gain = paths[cur_path][next_pos]

        # 이동 반영
        horses[h][0] = next_pos
        horses[h][1] = next_path
        score += gain
        i += 1

    return score

cases(0)
print(max_score)
