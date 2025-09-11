n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

ours = []
# get position
for i in range(n):
    for j in range(m):
        if 1 <= board[i][j] <= 5:
            # ours[i][0] = i번째 말의 종류
            # ours[i][1][0] = 해당 말의 i 좌표
            # ours[i][1][1] = 해당 말의 j 좌표
            ours.append([board[i][j], [i, j]])

directions = ['U', 'D', 'L', 'R']
d_case = []
temp_board = [[0] * m for _ in range(n)]
answer = m*n + 1
def create_case(cnt):
    global temp_board, answer
    if cnt == len(ours):
        for a in range(n):
            for b in range(m):
                temp_board[a][b] = board[a][b]
        answer = min(answer, get_area())
        return

    for d in directions:
        d_case.append(d)
        create_case(cnt + 1)
        d_case.pop()

def get_area():
    du, dl, dd, dr = [-1,0], [0,-1], [1,0], [0,1]
    for x in range(len(ours)):
        cur_horse, cur_d, cur_pos = ours[x][0], d_case[x], ours[x][1]
        if cur_horse == 1:
            if cur_d == 'U':
                move(cur_pos, [du])
            if cur_d == 'L':
                move(cur_pos, [dl])
            if cur_d == 'D':
                move(cur_pos, [dd])
            if cur_d == 'R':
                move(cur_pos, [dr])
        if cur_horse == 2:
            if cur_d == 'U' or cur_d == 'D':
                move(cur_pos, [du, dd])
            if cur_d == 'L' or cur_d == 'R':
                move(cur_pos, [dl, dr])
        if cur_horse == 3:
            if cur_d == 'U':
                move(cur_pos, [du, dr])   # ^>
            if cur_d == 'L':
                move(cur_pos, [dl, du])   # <^
            if cur_d == 'D':
                move(cur_pos, [dd, dl])   # <v
            if cur_d == 'R':
                move(cur_pos, [dr, dd])   # v>
        if cur_horse == 4:
            if cur_d == 'U':
                move(cur_pos, [du, dl, dr])   # <^>
            if cur_d == 'L':
                move(cur_pos, [dl, du, dd])   # <^v
            if cur_d == 'D':
                move(cur_pos, [dd, dr, dl])   # <v>
            if cur_d == 'R':
                move(cur_pos, [dr, du, dd])   # ^v>
        if cur_horse == 5:
            move(cur_pos, [du, dl, dd, dr])

    return get_answer()

# p : 말의 위치 / dirs : 방향 성분들 in list form
def move(p, dirs):
    # dir[0] = i 성분 / dir[1] = j 성분
    for d in dirs:
        l = 1
        while 0 <= p[0] + d[0]*l < n and 0 <= p[1] + d[1]*l < m:
            if board[p[0] + d[0]*l][p[1] + d[1]*l] == 6:
                break
            temp_board[p[0] + d[0]*l][p[1] + d[1]*l] = -1
            l += 1

def get_answer():
    count = 0
    for r in range(n):
        for c in range(m):
            if temp_board[r][c] == 0:
                count += 1
    return count

create_case(0)
print(answer)