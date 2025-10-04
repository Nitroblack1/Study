import sys
sys.stdin = open("input.txt", "r")
def debug(board):
    for r in board:
        for c in r:
            print(c, end=" ")
        print()
    print()


def modify():
    global ans
    temp_grid = [row[:] for row in grid]

    for i in range(len(layer)):
        temp_grid[layer[i]] = [char[i] for _ in range(w)]
    if test(temp_grid):
        ans = min(ans, len(layer))
        return


def test(t_map):
    for col in range(w):
        cnt, ok = 1, False
        for row in range(1, d):
            if t_map[row][col] == t_map[row-1][col]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= k:
                ok = True
                break
        if not ok:
            return False
    return True



def char_cases(cnt, r):
    if len(layer) >= ans:
        return

    if cnt == r:
        modify()
        return

    char.append(0)
    char_cases(cnt + 1, r)
    char.pop()

    char.append(1)
    char_cases(cnt + 1, r)
    char.pop()


def layer_cases(r, last_i, cnt):
    if cnt == r:
        char_cases(0, r)
        return

    for i in range(last_i, d):
        layer.append(i)
        layer_cases(r, i + 1, cnt + 1)
        layer.pop()


T = int(input())
for test_case in range(1, T + 1):
    layer, char = [], []
    d, w, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(d)]
    ans = d

    for r in range(d + 1):
        if ans <= r:
            break
        layer_cases(r, 0, 0)

    print(f'#{test_case} {ans}')