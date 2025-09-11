import sys

n = int(input())
world = [list(map(int, input().split())) for _ in range(n)]

answer = sys.maxsize
def d_pos():
    global answer
    for di in range(2, n):
        for dj in range(1, n - 1):
            for a in range(1, n):
                for b in range(1, n):
                    ri, rj = di - a, dj + a
                    ui, uj = di - a - b, dj + a - b
                    li, lj = di - b, dj - b
                    if is_inbound(ri, rj) and is_inbound(ui, uj) and is_inbound(li, lj):
                        answer = min(answer, get_tribes([[di, dj], [ri, rj], [ui, uj], [li, lj]]))


def is_inbound(r, c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


def get_tribes(points):
    d, r, u, l = points[0], points[1], points[2], points[3]
    t1, t2, t3, t4, t5 = 0, 0, 0, 0, 0

    # tribe 2 - fin
    i_depth_t2 = u[0] - 1
    for col in range(u[1], -1, -1):
        if col >= l[1]:
            i_depth_t2 += 1
        for row in range(0, i_depth_t2):
            t2 += world[row][col]

    # tribe 3 - fin
    i_depth_t3 = u[0]
    for col in range(u[1] + 1, n):
        if col <= r[1] + 1:
            i_depth_t3 += 1
        for row in range(0, i_depth_t3):
            t3 += world[row][col]

    # tribe 4 - fin
    i_height_t4 = d[0] + 1
    for col in range(d[1] - 1, -1, -1):
        if col >= l[1] - 1:
            i_height_t4 -= 1
        for row in range(i_height_t4, n):
            t4 += world[row][col]

    #tribe 5
    i_height_t5 = d[0] + 2
    for col in range(d[1], n):
        if col <= r[1]:
            i_height_t5 -= 1
        for row in range(i_height_t5, n):
            t5 += world[row][col]

    # tribe 1
    total = 0
    for i in range(n):
        for j in range(n):
            total += world[i][j]
    t1 = total - (t2 + t3 + t4 + t5)

    return max(t1, t2, t3, t4, t5) - min(t1, t2, t3, t4, t5)

d_pos()
print(answer)