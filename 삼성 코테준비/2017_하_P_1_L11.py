################## SET UP ##################
t1 = input()
t2 = input()
t3 = input()
t4 = input()
table1, table2, table3, table4 = [], [], [], []

for num in t1:
    table1.append(int(num))

for num in t2:
    table2.append(int(num))

for num in t3:
    table3.append(int(num))

for num in t4:
    table4.append(int(num))

tables = [table1, table2, table3, table4]

k = int(input())
turn_info = []
for _ in range(k):
    # turn_info[i][0], turn_info[i][1] : i번째 회전 정보
    turn_info.append(list(map(int, input().split())))

################## SET UP Fin ##################
from collections import deque

def check_linkage(cur_t, d):
    if cur_t == 3:
        if d == -1 and tables[2][2] != tables[3][6]:
            return True
        else:
            return False
    if cur_t == 2:
        if d == -1 and tables[1][2] != tables[2][6]:
            return True
        if d == 1 and tables[3][6] != tables[2][2]:
            return True
        else:
            return False
    if cur_t == 1:
        if d == -1 and tables[0][2] != tables[1][6]:
            return True
        if d == 1 and tables[2][6] != tables[1][2]:
            return True
        else:
            return False
    if cur_t == 0:
        if d == 1 and tables[1][6] != tables[0][2]:
            return True
        return False
    return False

def rotate(table_no, direction):
    if direction == 1:
        temp = tables[table_no][7]
        for x in range(7, 0, -1):
            tables[table_no][x] = tables[table_no][x-1]
        tables[table_no][0] = temp
    elif direction == -1:
        temp = tables[table_no][0]
        for x in range(7):
            tables[table_no][x] = tables[table_no][x+1]
        tables[table_no][7] = temp

q = deque()
dis = [1, -1]
# turn
for turn in turn_info:
    # turn[0] : 테이블 번호 / turn[1] : 방향
    # tables[i] -> i = turn[0] - 1
    is_linked = [False] * 4
    q.append(turn[0] - 1)
    while q:
        cur_i = q.popleft()
        is_linked[cur_i] = True
        for di in dis:
            new_i = cur_i + di
            if check_linkage(cur_i, di) and not is_linked[new_i]:
                q.append(new_i)

    for i in range(4):
        if not is_linked[i]:
            continue
        elif is_linked[i] and turn[0] % 2 == (i+1) % 2:
            rotate(i, turn[1])
        elif is_linked[i] and turn[0] % 2 != (i+1) % 2:
            rotate(i, -1 * turn[1])

# get answer
answer = 0
for i in range(4):
    if tables[i][0] == 1:
        answer += pow(2, i) * 1

print(answer)