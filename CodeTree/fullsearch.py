n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 0,0부터 시작해서 직사각형을 넓혀 나가다가 음수를 만나면 해당 방향 확장 멈춤

best = 0

for top in range(n):
    for left in range(m):
        for bottom in range(n):
            for right in range(m):
                area = (top-bottom+1)*(left-right+1)
                if area <= best:
                    continue

                all_pos = True
                for r in range(top, bottom+1):
                    for c in range(left, right+1):
                        if grid[r][c] < 0:
                            all_pos = False
                            break
                    if not all_pos:
                        break
                if all_pos:
                    best = area

print(best)

def positive_rect(x1, y1, x2, y2):
    return all([
        grid[i][j] > 0
        for i in range(x1, x2+1)
        for j in range(y1, y2+1)
    ])

ans = -1

for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                if positive_rect(i, j, k, l):
                    ans = max(ans, (k-i+1)*(l-j+1))

print(ans)