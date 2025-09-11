n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r) - 1, d) for r, d in [input().split() for _ in range(q)]]

# Please write your code here.
# r행에 대해 d방향으로 shift
def shift(r, d):
    if d == 1:
        temp = a[r][m-1]
        for i in range(m-1, 0, -1):
            a[r][i] = a[r][i-1]
        a[r][0] = temp
    elif d == -1:
        temp = a[r][0]
        for i in range(0, m-1):
            a[r][i] = a[r][i+1]
        a[r][m-1] = temp


# 두 행간 전파 조건 체크
def is_linked(row_a, row_b):
    for elem_a, elem_b in zip(row_a, row_b):
        if elem_a == elem_b:
            return True
    return False

for wind in winds:
    if wind[1] == 'L':
        d = 1
    else :
        d = -1

    shift(wind[0], d)
    up_d, down_d = d, d

    up, down = 1, 1
    while wind[0] - up >= 0:   # 상한선
        if is_linked(a[wind[0] - up + 1], a[wind[0] - up]):
            shift(wind[0]-up, -1*up_d)
            up_d = -1 * up_d  # 역방향 저장
        else:
            break
        up += 1

    while wind[0] + down < n:   # 하한선
        if is_linked(a[wind[0] + down - 1], a[wind[0] + down]):
            shift(wind[0]+down, -1*down_d)
            down_d = -1 * down_d
        else:
            break
        down += 1

for row in a:
    for element in row:
        print(element, end=" ")
    print()