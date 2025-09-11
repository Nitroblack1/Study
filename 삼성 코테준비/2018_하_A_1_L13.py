import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
food = [list(map(int, input().split())) for _ in range(n)]
badge = [[5]*n for _ in range(n)]

# 칸별 나이 오름차순 deque
trees = [[deque() for _ in range(n)] for __ in range(n)]

for _ in range(m):
    r, c, age = map(int, input().split())
    trees[r-1][c-1].append(age)

# 초기에도 칸별로 정렬해두면 안정적
for i in range(n):
    for j in range(n):
        if trees[i][j]:
            trees[i][j] = deque(sorted(trees[i][j]))

dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

for _ in range(k):
    breed_cnt = [[0]*n for _ in range(n)]  # 가을 번식용 카운트

    # 봄 + 여름
    for i in range(n):
        for j in range(n):
            if not trees[i][j]:
                continue
            q = trees[i][j]
            survivors = deque()
            added = 0     # 여름: 죽은 개체가 남긴 양분
            nutrient = badge[i][j]

            # 나이 오름차순으로 이미 정렬되어 있음
            while q:
                age = q.popleft()
                if nutrient >= age:
                    nutrient -= age
                    new_age = age + 1
                    survivors.append(new_age)
                    if new_age % 5 == 0:
                        breed_cnt[i][j] += 1
                else:
                    # 즉시 여름 처리: 죽은 나이//2 누적
                    added += (age // 2)
                    # 뒤쪽 남은 애들도 전부 죽지만,
                    # 여기서는 이미 오름차순이라 뒤는 더 나이 많음 → 다 못 먹음
                    while q:
                        a2 = q.popleft()
                        added += (a2 // 2)
                    break

            badge[i][j] = nutrient + added
            trees[i][j] = survivors

    # 가을(번식)
    for i in range(n):
        for j in range(n):
            cnt = breed_cnt[i][j]
            if cnt == 0:
                continue
            ones = [1]*cnt
            for dx, dy in dirs:
                ni, nj = i+dx, j+dy
                if 0 <= ni < n and 0 <= nj < n:
                    # 1살이 가장 어린 나이 → 왼쪽에 붙이면 정렬 유지
                    trees[ni][nj].extendleft(ones)

    # 겨울(양분 공급)
    for i in range(n):
        bi = badge[i]
        fi = food[i]
        for j in range(n):
            bi[j] += fi[j]

# 정답: 살아있는 개체 수
ans = 0
for i in range(n):
    for j in range(n):
        ans += len(trees[i][j])
print(ans)
