n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


sweep_directions = ['L', 'R', 'U', 'D']
sweep_list = []
answer = 0

# 5번 스윕할 수 있는 모든 경우의 수 생성
def gen_sweep_cases(cnt):
    global answer
    if cnt == 5:
        answer = max(answer, find_max_block(sweep()))
        return

    for directions in sweep_directions:
        sweep_list.append(directions)
        gen_sweep_cases(cnt+1)
        sweep_list.pop()

    return

# sweep 방향으로 중력이 작용한다.
# 바닥에서 가까운 숫자부터 2개씩만 합쳐진다.
# 4^5 경우의 수에 대한 실제 sweep 결과 계산
def sweep():
    temp = []
    for row in grid:
        temp.append(row)
    for d in sweep_list:
        if d == 'L':
            gravity_on_l(temp)
        if d == 'R':
            gravity_on_r(temp)
        if d == 'U':
            gravity_on_u(temp)
        if d == 'D':
            gravity_on_d(temp)

    return temp

def gravity_on_l(t):
    # 중력 작용
    for i in range(n):
        temp_row, x = [0 for _ in range(n)], 0
        for j in range(n):
            if t[i][j] != 0:
                temp_row[x] = t[i][j]
                x += 1
        # 같은 수가 있으면 합치고, L로 당긴다.
        for a in range(n-1):
            if temp_row[a] == temp_row[a+1]:
                temp_row[a] *= 2
                for b in range(a+1, n-1):
                    temp_row[b] = temp_row[b+1]
                temp_row[n-1] = 0
        # 원본에 복사
        t[i] = temp_row

def gravity_on_r(t):
    # 중력 작용
    for i in range(n):
        temp_row, x = [0 for _ in range(n)], n-1
        for j in range(n-1, -1, -1):
            if t[i][j] != 0:
                temp_row[x] = t[i][j]
                x -= 1
        # 같은 수가 있으면 합치고, R로 당긴다.
        for a in range(n-1, 0, -1):
            if temp_row[a] == temp_row[a-1]:
                temp_row[a] *= 2
                for b in range(a-1, -1, -1):
                    temp_row[b] = temp_row[b-1]
                temp_row[0] = 0
        # 원본에 복사
        t[i] = temp_row

def gravity_on_u(t):
    # 중력 작용
    for j in range(n):
        temp_col, x = [0 for _ in range(n)], 0
        for i in range(n):
            if t[i][j] != 0:
                temp_col[x] = t[i][j]
                x += 1
        # 같은 수가 있으면 합치고, U로 당긴다.
        for a in range(n-1):
            if temp_col[a] == temp_col[a+1]:
                temp_col[a] *= 2
                for b in range(a+1, n-1):
                    temp_col[b] = temp_col[b+1]
                temp_col[n-1] = 0
        # 원본에 복사
        for row in range(n):
            t[row][j] = temp_col[row]

def gravity_on_d(t):
    # 중력 작용
    for j in range(n):
        temp_col, x = [0 for _ in range(n)], n - 1
        for i in range(n - 1, -1, -1):
            if t[i][j] != 0:
                temp_col[x] = t[i][j]
                x -= 1
        # 같은 수가 있으면 합치고, D로 당긴다.
        for a in range(n - 1, 0, -1):
            if temp_col[a] == temp_col[a - 1]:
                temp_col[a] *= 2
                for b in range(a - 1, -1, -1):
                    temp_col[b] = temp_col[b - 1]
                temp_col[0] = 0
        # 원본에 복사
        for row in range(n):
            t[row][j] = temp_col[row]


def find_max_block(t):
    max_value = 0
    for row in t:
        for elem in row:
            if elem > max_value:
                max_value = elem
    return max_value

gen_sweep_cases(0)
print(answer)