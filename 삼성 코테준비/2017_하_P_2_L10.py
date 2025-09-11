n = int(input())
nums = list(map(int, input().split()))
# ops[0] : + / ops[1] : - / ops[2] : *
ops = list(map(int, input().split()))

min_ans = 1000000001
max_ans = -1 * min_ans

def calculate():
    result = nums[0]
    for i in range(n-1):
        if ops_list[i] == '+':
            result += nums[i+1]
        if ops_list[i] == '-':
            result -= nums[i+1]
        if ops_list[i] == '*':
            result *= nums[i+1]
    return result

ops_list = []
def cases(cnt):
    global max_ans, min_ans
    if cnt == n-1:
        max_ans = max(max_ans, calculate())
        min_ans = min(min_ans, calculate())
        return

    if ops_list.count('+') < ops[0]:
        ops_list.append('+')
        cases(cnt+1)
        ops_list.pop()

    if ops_list.count('-') < ops[1]:
        ops_list.append('-')
        cases(cnt + 1)
        ops_list.pop()

    if ops_list.count('*') < ops[2]:
        ops_list.append('*')
        cases(cnt + 1)
        ops_list.pop()


cases(0)
print(min_ans, max_ans)


########### DFS ###########
# n = int(input())
# numbers = list(map(int, input().split()))
# plus, minus, product = map(int, input().split())
# answer = []
#
# def dfs(idx, plus, minus, product, ans):
#     if idx == len(numbers) - 1:
#         answer.append(ans)
#         return
#     if plus != 0:
#         dfs(idx+1, plus - 1, minus, product, ans + numbers[idx+1])
#     if minus != 0:
#         dfs(idx+1, plus, minus - 1, product, ans - numbers[idx+1])
#     if product != 0:
#         dfs(idx+1, plus, minus, product - 1, ans * numbers[idx+1])
#
#
# dfs(0, plus, minus, product, numbers[0])
# print(min(answer), max(answer))