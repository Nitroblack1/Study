n, k = map(int, input().split())
temp = list(map(int, input().split()))
road = []
for t in temp:
    road.append([t, False])

def rotate():
    global road
    road = [road[-1]] + road[:-1]

    return

def forward():
    # 맨 끝 칸은 어차피 바로 내리고, 맨 앞 칸은 어차피 회전 후에 올라오므로
    # 검사할 필요 X
    for idx in range(n-2, 0, -1):
        # 우선 사람이 있는 곳을 찾아서
        if road[idx][1]:
            # 만약 앞 칸이 이동가능한 곳이라면
            if is_available(idx + 1):
                road[idx + 1][1] = True
                road[idx][1] = False
                decrease_safety(idx + 1)
    return

def is_available(index):
    # 안정성이 0보다 크고, 사람이 없다면
    if road[index][0] > 0 and not road[index][1]:
        return True
    return False

# 올라가는 위치는 0으로 고정. 따라서 param 안받음.
def onboard():
    road[0][1] = True
    decrease_safety(0)
    return

# 도착칸은 n-1로 고정. 따라서 param 안받음.
def drop():
    if road[n-1][1]:
        road[n-1][1] = False
    return

def decrease_safety(index):
    road[index][0] -= 1
    return

def safety_check():
    count = 0
    for tile in road:
        if tile[0] == 0:
            count += 1

    if count >= k:
        return False
    else:
        return True

turn = 0
def experiment():
    global turn
    while safety_check():
        rotate()
        drop()

        forward()
        drop()

        if is_available(0):
            onboard()

        turn += 1

    return

experiment()
print(turn)