from collections import deque
import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

hospitals = list()
selected_hos = list()

# bfs에 필요한 변수들 입니다.
q = deque()
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
step = [
    [False for _ in range(n)]
    for _ in range(n)
]

ans = INT_MAX


# 범위가 격자 안에 들어가는지 확인합니다.
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# 범위를 벗어나지 않으면서 벽이 아니고, 방문한적이 없어야 갈 수 있습니다.
def can_go(x, y):
    return in_range(x, y) and a[x][y] != 1 and not visited[x][y]


# queue에 새로운 위치를 추가하고 방문 여부를 표시해줍니다.
# 시작점으로 부터의 최단거리 값도 갱신해줍니다.
def push(x, y, new_step):
    q.append((x, y))
    visited[x][y] = True
    step[x][y] = new_step


# visited, step 배열을 초기화합니다.
def initialize():
    for i in range(n):
        for j in range(n):
            visited[i][j] = step[i][j] = 0


# BFS를 통해 선택된 병원들로부터
# 가장 거리가 먼 바이러스까지의 거리를 구합니다.
def find_max_dist():
    while q:
        # queue에서 가장 먼저 들어온 원소를 뺍니다.
        x, y = q.popleft()

        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

        # queue에서 뺀 원소의 위치를 기준으로 4 방향을 확인합니다.
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            # 더 갈 수 있는 곳이라면 Queue에 추가합니다.
            if can_go(new_x, new_y):
                # 최단 거리는 이전 최단거리에 1이 증가하게 됩니다.
                push(new_x, new_y, step[x][y] + 1)

    # 바이러스들 까지의 거리들 중 가장 먼 거리를 기록합니다.
    max_dist = 0

    for i in range(n):
        for j in range(n):
            # 바이러스인 경우에만 거리를 갱신합니다.
            if a[i][j] == 0:
                if visited[i][j]:
                    max_dist = max(max_dist, step[i][j])
                # 만약 선택한 병원 조합으로는 해당 바이러스에 도달이 불가능하다면
                # 도달이 불가능 하다는 표시로 INT_MAX를 넣어줍니다.
                else:
                    max_dist = INT_MAX

    return max_dist


# 선택된 병원으로부터 모든 바이러스를 없애기 위해 걸리는 시간을 계산합니다.
def elapsed_time_to_kill_all_virus():
    # BFS를 다시 돌리기 전에 visited, step 배열을 초기화합니다.
    initialize()

    # 선택된 병원들을 시작으로 하여 BFS를 한 번 돌립니다.
    for i in range(len(selected_hos)):
        x, y = selected_hos[i]
        push(x, y, 0)

    max_elapsed_time = find_max_dist()
    return max_elapsed_time


# Backtracking을 이용하여 m개의 병원을 전부 선택해 봐서
# 그 중 모든 바이러스를 없애는 데 걸리는 시간 중 최소 시간을 구합니다.
def find_min_time(curr_idx, cnt):
    global ans

    if cnt == m:
        # 선택된 병원으로부터 모든 바이러스를 없애기 위해
        # 걸리는 시간을 계산하여 답보다 더 좋은 경우 갱신해줍니다.
        ans = min(ans, elapsed_time_to_kill_all_virus())
        return

    if curr_idx == len(hospitals):
        return

    find_min_time(curr_idx + 1, cnt)

    selected_hos.append(hospitals[curr_idx])
    find_min_time(curr_idx + 1, cnt + 1)
    selected_hos.pop()


# Backtracking을 선택할 병원 index 기준으로 쉽게 돌리기 위해 병원 위치만 따로 저장합니다.
for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            hospitals.append((i, j))

# 최소 시간을 구합니다.
find_min_time(0, 0)
if ans == INT_MAX:
    ans = -1

print(ans)