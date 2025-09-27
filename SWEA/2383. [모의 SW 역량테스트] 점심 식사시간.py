import sys
sys.stdin = open("input.txt", "r")
from collections import deque

# 계단 시뮬레이션 함수
def simulate(assign, dist, stairs):
    results = [0, 0]  # stair별 완료 시간

    for si in (0, 1):
        arrivals = [dist[pi][si] for pi, a in enumerate(assign) if a == si]
        if not arrivals:
            continue
        arrivals.sort()
        length = stairs[si][2]

        q = deque()  # 계단 위 사람들의 "끝나는 시간"
        finish_times = []

        for t in arrivals:
            arrive_time = t + 1  # 계단 입구 도착 후 1분 후 입장
            # 계단에 공간이 남으면 바로 입장
            if len(q) < 3:
                start = arrive_time
            else:
                # 계단이 꽉 찼으면 가장 먼저 끝나는 사람을 기다림
                first_finish = q.popleft()
                start = max(arrive_time, first_finish)
            end = start + length
            finish_times.append(end)

            # 종료 시간을 다시 정렬된 상태로 넣음
            inserted = False
            for i in range(len(q)):
                if end < q[i]:
                    q.insert(i, end)
                    inserted = True
                    break
            if not inserted:
                q.append(end)

        results[si] = max(finish_times)
    return max(results)


def dfs(idx, assign, dist, stairs, P):
    global ans
    if idx == P:
        total_time = simulate(assign, dist, stairs)
        ans = min(ans, total_time)
        return

    assign[idx] = 0
    dfs(idx + 1, assign, dist, stairs, P)

    assign[idx] = 1
    dfs(idx + 1, assign, dist, stairs, P)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stairs = []
    for i in range(N):
        for j in range(N):
            if room[i][j] == 1:
                people.append((i, j))
            elif room[i][j] > 1:
                stairs.append((i, j, room[i][j]))  # (row, col, length)

    P = len(people)

    # 거리 계산 (맨해튼 거리)
    dist = [[0] * 2 for _ in range(P)]
    for pi, (pr, pc) in enumerate(people):
        for si, (sr, sc, length) in enumerate(stairs):
            dist[pi][si] = abs(pr - sr) + abs(pc - sc)

    ans = 10**9
    assign = [0] * P
    dfs(0, assign, dist, stairs, P)

    print(f"#{tc} {ans}")
