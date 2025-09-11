import sys

MAX_HOSPITAL = 13
INT_MAX = sys.maxsize

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
given_map = [
    list(map(int, input().split()))
    for _ in range(n)
]
people = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if given_map[i][j] == 1
]
hospitals = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if given_map[i][j] == 2
]
visited = [
    False for _ in range(MAX_HOSPITAL)
]

min_distance = INT_MAX


# 사람과 병원 사이의 거리를 구하여 반환해줍니다.
def get_distance(person, hospital):
    px, py = person
    hx, hy = hospital
    return abs(px - hx) + abs(py - hy)


# m개의 병원이 선택됐을 때 각 사람의 병원 거리에 대한 합을 반환해줍니다.
def get_curr_min_distance():
    curr_min_distance = 0

    # 각 사람에 대하여 가장 가까운 병원의 거리를 구합니다.
    for person in people:
        single_min = min([
            get_distance(person, hospital)
            for i, hospital in enumerate(hospitals)
            if visited[i]
        ])
        curr_min_distance += single_min

    return curr_min_distance


def search_min_distance(cnt, last_idx):
    global min_distance

    # m개의 병원이 선택되었을 경우 병권 거리의 총합을 구해줍니다.
    if cnt == m:
        min_distance = min(min_distance, get_curr_min_distance())
        return

    # 뽑을 수 있는 병원의 후보들을 탐색합니다.
    for i in range(last_idx + 1, len(hospitals)):
        visited[i] = True
        search_min_distance(cnt + 1, i)
        visited[i] = False


search_min_distance(0, -1)
print(min_distance)