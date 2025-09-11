# k, n = map(int, input().split())
#
#
# def print_answer():
#     for elem in answer:
#         print(elem, end=" ")
#     print()
#
# answer = []
# def choose(curr_num):
#     if curr_num == n:
#         print_answer()
#         return
#
#     for select in range(1, k+1):
#         answer.append(select)
#         choose(curr_num + 1)
#         answer.pop()
#
#     return
#
# choose(0)

#########################################################################################################
n = int(input())

ans = 0
seq = []
# Please write your code here.

def check():
    i = 0
    while i < n:
        if i + seq[i] - 1 >= n:
            return False

        for j in range(i, i + seq[i]):
            if seq[j] != seq[i]:
                return False

        i += seq[i]

    return True

def count_beautiful_seq(cnt):
    global ans

    if cnt == n:
        if check():
            ans += 1
        return

    for i in range(1,5):
        seq.append(i)
        count_beautiful_seq(cnt+1)
        seq.pop()


count_beautiful_seq(0)
print(ans)