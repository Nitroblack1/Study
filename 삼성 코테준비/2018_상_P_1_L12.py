n = int(input())
initial_lines = []
for _ in range(n):
    initial_lines.append(list(map(int, input().split())))

# 0 : R / 1 : U / 2 : L / 3 : D
# 90도 회전 공식
# X_e = X_c + (Y_s - Y_c)
# Y_e = Y_c - (X_s - X_c)

points = []
def draw(info):
    cur_points = []
    x, y, d, g = info[0], info[1], info[2], info[3]
    cur_points.append((x,y))
    if d == 0:
        cur_points.append((x, y + 1))
    if d == 1:
        cur_points.append((x - 1, y))
    if d == 2:
        cur_points.append((x, y - 1))
    if d == 3:
        cur_points.append((x + 1, y))
    end_point = cur_points[-1]

    # 1차부터 적용
    for _ in range(g):
        for i in range(len(cur_points) - 2, -1, -1):
            x_s, y_s = cur_points[i][0], cur_points[i][1]
            x_c, y_c = end_point[0], end_point[1]
            x_e = x_c + (y_s - y_c)
            y_e = y_c - (x_s - x_c)
            cur_points.append((x_e, y_e))
        end_point = cur_points[-1]
    return cur_points

def get_square():
    answer = 0
    for a in range(len(points) - 3):
        # 오른쪽 확인
        if points[a + 1] == (points[a][0], points[a][1] + 1):
            for b in range(a + 2, len(points) - 1):
                # a 아랫쪽 확인
                if points[b] == (points[a][0] + 1, points[a][1]):
                    # 대각선 확인
                    if points[b+1] == (points[a][0] + 1, points[a][1] + 1):
                        answer += 1

    return answer

for line in initial_lines:
    points += draw(line)

# 중복 원소 제거
points = list(set(points))
# x 오름차순, y 오름차순 정렬
points.sort(key=lambda x: (x[0], x[1]))

print(get_square())