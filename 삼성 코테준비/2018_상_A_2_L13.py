n, m, h = map(int, input().split())

answer = 4
ll = []
# 0행, 0열은 False -> index 1로 initialize
# line_map = [[False] * n for _ in range(h + 1)]
for _ in range(m):
    ll.append(list(map(int, input().split())))

ll.sort(key=lambda x: [x[1], x[0]])
brackets = [[] for _ in range(n)]
for l in ll:
    # a~a+1 연결 의미
    brackets[l[1]].append(l[0])

print(brackets)

def calculate(la, lb):
    s = 0
    a_i, b_i = 0, 0
    while a_i < len(la) and b_i < len(lb):
        if la == lb:
            return -1

        if la[a_i] < lb[b_i]:
            s += 1
            a_i += 1
        else:
            s -= 1
            b_i += 1

    # 남은 거 처리
    if a_i == len(la):
        while b_i < len(lb):
            s -= 1
            b_i += 1
    if b_i == len(lb):
        while a_i < len(la):
            s += 1
            a_i += 1

    # 비대칭량 리턴
    return s

for i in range(n):
    if not brackets[i]:
        continue
    if brackets[i] and not brackets[i+1]:
        continue
    calculate(brackets[i], brackets[i + 1])


if answer == 4:
    print(-1)
else:
    print(answer)