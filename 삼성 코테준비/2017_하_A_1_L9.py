n = int(input())
synergy = [list(map(int, input().split())) for _ in range(n)]

am_work, pm_work = [], []
answer = 10000
i = 0

def bt_for_schedule(cnt):
    global answer, i
    if cnt == n:
        if len(am_work) == int(n/2) and len(pm_work) == int(n/2):
            answer = min(answer, abs(bt_for_cal(am_work) - bt_for_cal(pm_work)))
        return

    am_work.append(i)
    i += 1
    bt_for_schedule(cnt + 1)
    am_work.pop()
    i -= 1

    pm_work.append(i)
    i += 1
    bt_for_schedule(cnt + 1)
    pm_work.pop()
    i -= 1

    return


def bt_for_cal(w):
    d = 0
    for i in range(len(w) - 1):
        for j in range(i+1, len(w)):
            d += synergy[w[i]][w[j]] + synergy[w[j]][w[i]]

    return d


bt_for_schedule(0)
print(answer)