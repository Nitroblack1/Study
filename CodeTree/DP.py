### Basic Concept of DP memoization (recursive function)
# n = int(input())
# memo = [-1] * (n+1)
#
# def fibbo(x):
#     if memo[x] != -1:
#         return memo[x]
#
#     if x <= 2:
#         memo[x] = 1
#     else:
#         memo[x] = fibbo(x-1) + fibbo(x-2)
#
#     return memo[x]
#
# print(fibbo(n))

### Basic Concept of DP Tabulation (for loop)
# N = int(input())
#
# def fibbo(n):
#   arr = [-1] * (n+1)
#   arr[1] = 1
#   arr[2] = 1
#   for i in range(3, n+1):
#       arr[i] = arr[i-1] + arr[i-2]
#       print(arr[i])
#
#   return arr[n]
#
# print(fibbo(N))

### 정수 사각형 from CodeTree Problem
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * N for _ in range(N)]
dp[0][0] = grid[0][0]

for i in range(0, N):
    for j in range(0, N):
        if i == 0 and j == 0:
            dp[i][j] = grid[i][j]
        else:
            dp[i][j] = max(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])

print(dp[N-1][N-1])