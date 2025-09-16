from collections import deque

n, m = map(int, input().split())
base_map = [list(map(int, input().split())) for _ in range(n)]
stores = [list(map(int, input().split())) for _ in range(m)]

# move available map
# If it's False, it's not available
avail_map = [
    [True for _ in range(n)]
    for _ in range(n)
]

# indexing at 0
for store in stores:
    store[0] -= 1
    store[1] -= 1

# initialize people's indices and arrived.
p_indices = [[-1, -1, False] for _ in range(m)]
p_path = [
    [] for _ in range(m)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]


################### minor ###################
dis, djs = [-1, 0, 0, 1], [0, -1, 1, 0]

def debug(board):
    for r in board:
        for c in r:
            print(int(c), end=" ")
        print()
    print()

def started(i, j):
    if i != -1 and j != -1:
        return True
    return False

def inbound(i, j):
    if 0 <= i < n and 0 <= j < n:
        return True
    return False

# '이동' 가능한 곳인지
def can_go(i, j):
    if inbound(i, j) and avail_map[i][j]:
        return True
    return False

def initialize_visited():
    global visited
    visited = [
        [False for _ in range(n)]
        for _ in range(n)
    ]
################### minor ###################


def simulate():
    finished = False
    need_update = False

    minute = 1
    while not finished:
        # print('min ', minute)
        finished = True
        banned_area = []

        # if base camp or store is occupied

        noob = -1
        for i, p in enumerate(p_indices):
            # if the player goaled, pass
            if p[2]:
                continue

            finished = False

            # 1) move
            if started(p[0], p[1]):
                if need_update:
                    p_path[i] = get_path([p[0], p[1]], [stores[i][0], stores[i][1]])
                    # print('changed.')
                    # print(p_path)
                p[0], p[1] = p_path[i].pop()

                if p[0] == stores[i][0] and p[1] == stores[i][1]:
                    p[2] = True
                    banned_area.append([p[0], p[1]])
                    # print(i, 'arrived')
                    need_update = True
            else:
                noob = i
                break

        if banned_area:
            for area in banned_area:
                avail_map[area[0]][area[1]] = False

        # if it's noob
        if noob != -1:
            base_camp = get_base_camp(stores[noob])
            p_indices[noob][0], p_indices[noob][1] = base_camp[0], base_camp[1]
            avail_map[base_camp[0]][base_camp[1]] = False

            p_path[noob] = get_path(base_camp, stores[noob])


        if finished:
            return minute

        minute += 1
        # for i in range(m):
        #     print(p_indices[i], stores[i])
        # debug(avail_map)

    return -1


# from store to base camp
def get_base_camp(st):
    global visited
    q = deque()
    initialize_visited()

    base_list = []
    min_dis = 100
    finished = False

    visited[st[0]][st[1]] = True
    q.append((st[0], st[1], 0))
    while q and not finished:
        ci, cj, cd = q.popleft()
        for di, dj in zip(dis, djs):
            ni, nj, nd = ci + di, cj + dj, cd + 1
            # nd가 min보다 커지는 시점에서는 끝내야 함.
            if nd > min_dis:
                finished = True
                break
            if can_go(ni, nj) and not visited[ni][nj]:
                if base_map[ni][nj] == 1:
                    base_list.append([ni, nj])
                    min_dis = nd
                    visited[ni][nj] = True
                else:
                    q.append((ni, nj, nd))
                    visited[ni][nj] = True

    base_list.sort(key=lambda x: [x[0], x[1]])
    return base_list[0]


def get_path(start, end):
    global visited
    q = deque()
    initialize_visited()

    from_where = [
        [[-1, -1] for _ in range(n)]
        for _ in range(n)
    ]
    finished = False

    visited[start[0]][start[1]] = True
    q.append((start[0], start[1]))
    from_where[start[0]][start[1]] = [start[0], start[1]]
    while q and not finished:
        ci, cj = q.popleft()
        for di, dj in zip(dis, djs):
            ni, nj = ci + di, cj + dj
            if can_go(ni, nj) and not visited[ni][nj]:
                if ni == end[0] and nj == end[1]:
                    from_where[ni][nj] = [ci, cj]
                    finished = True
                    break
                q.append((ni, nj))
                visited[ni][nj] = True
                from_where[ni][nj] = [ci, cj]

    ci, cj = end[0], end[1]
    path = []
    while ci != start[0] or cj != start[1]:
        path.append([ci, cj])
        ci, cj = from_where[ci][cj]

    return path




####################### Main #######################
print(simulate() - 1)