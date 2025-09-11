from collections import deque

# k : # of mold
n, m, k = map(int, input().split())

# x, y : mold pos / s : dis per sec of mold / d : dir / b : size of mold
molds = []
answer = 0

for _ in range(k):
    # molds[i][0] : i'th mold's i pos / ...
    molds.append(list(map(int, input().split())))


# collect nearest mold in col
def collect():
    global answer, molds
    molds.sort(key=lambda x: [x[1], x[0]])
    # index starts from 1!
    for col in range(1, m + 1):
        for mold in molds:
            # if there's mold in search area(col)
            if mold[1] == col:
                # print('collected ', mold)
                answer += mold[4]
                molds.remove(mold)
                break
            # if no mold, pass
            else:
                continue
        move()
        molds = collision_check()

# molds move
def move():
    for mold in molds:
        if mold[4] == 0:
            continue
        d = 0
        while d != mold[2]:
            # Up
            if mold[3] == 1:
                if mold[0] > 1:
                    mold[0] -= 1
                else:
                    mold[3] = 2
                    mold[0] += 1
                d += 1
                continue
            # Down
            if mold[3] == 2:
                if mold[0] < n:
                    mold[0] += 1
                else:
                    mold[3] = 1
                    mold[0] -= 1
                d += 1
                continue
            # Right
            if mold[3] == 3:
                if mold[1] < m:
                    mold[1] += 1
                else:
                    mold[3] = 4
                    mold[1] -= 1
                d += 1
                continue
            # Left
            if mold[3] == 4:
                if mold[1] > 1:
                    mold[1] -= 1
                else:
                    mold[3] = 3
                    mold[1] += 1
                d += 1
                continue


def collision_check():
    molds.sort(key=lambda x: [x[0], x[1], -x[4]])
    l = 0
    for i in range(len(molds) - 1):
        cur_i, cur_j, cur_s = molds[i][0], molds[i][1], molds[i][4]
        for j in range(i + 1, len(molds)):
            if molds[j][4] != 0 and cur_i == molds[j][0] and cur_j == molds[j][1]:
                # print('killed mold is ', molds[j])
                molds[j][0], molds[j][1], molds[j][4] = -1, -1, 0
                l += 1
            else:
                break

    molds.sort(key=lambda x: [x[0], x[1]])
    return molds[l:]


collect()
print(answer)