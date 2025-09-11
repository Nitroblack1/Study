n = int(input())
# works[i][0] : i일에 주어진 일의 기한 t / works[i][1] : ~ 수익 p
works = [list(map(int, input().split())) for _ in range(n)]

work_selection = []
answer = 0
# 각 일에 대해 O, X 여부를 전부 생성하여 전달
def generate_work_selection(cnt):
    global answer
    if cnt == 15:
        answer = max(answer, calculate())
        return

    work_selection.append(1)
    generate_work_selection(cnt+1)
    work_selection.pop()

    work_selection.append(0)
    generate_work_selection(cnt+1)
    work_selection.pop()
    return


def calculate():
    cur_fin_time = -1
    income = 0
    for i in range(n):
        if work_selection[i] == 1 and i > cur_fin_time:
            if i + works[i][0] <= n:
                cur_fin_time = i + works[i][0] - 1
                income += works[i][1]
    return income

generate_work_selection(0)
print(answer)

##### test case #####
# 9
# 5 2
# 5 1
# 5 1
# 5 1
# 5 1
# 5 1
# 5 1
# 5 1
# 5 1
