import sys
sys.stdin = open("input.txt", "r")

# 방향: 상(1), 하(2), 좌(3), 우(4)
dss = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
reverse = {1: 2, 2: 1, 3: 4, 4: 3}

def simulate(colonies, n, m):
    for _ in range(m):
        new_map = {}

        # 1. 모든 군집 이동
        for r, c, cnt, d in colonies:
            nr, nc = r + dss[d][0], c + dss[d][1]

            # 2. 경계 처리
            if nr == 0 or nr == n - 1 or nc == 0 or nc == n - 1:
                cnt //= 2
                d = reverse[d]
                if cnt == 0:
                    continue  # 군집 소멸

            # 3. 새 위치에 저장
            if (nr, nc) not in new_map:
                new_map[(nr, nc)] = []
            new_map[(nr, nc)].append((cnt, d))

        # 4. 군집 합치기
        colonies = []
        for (r, c), groups in new_map.items():
            if len(groups) == 1:
                colonies.append((r, c, groups[0][0], groups[0][1]))
            else:
                total = sum(g[0] for g in groups)
                # 가장 큰 군집의 방향 선택
                _, max_d = max(groups, key=lambda x: x[0])
                colonies.append((r, c, total, max_d))

    return colonies


T = int(input())
for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    colonies = []
    for _ in range(k):
        r, c, cnt, d = map(int, input().split())
        colonies.append((r, c, cnt, d))

    colonies = simulate(colonies, n, m)
    ans = sum(c[2] for c in colonies)
    print(f"#{tc} {ans}")