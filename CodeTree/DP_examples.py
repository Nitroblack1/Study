N = int(input())

# Please write your code here.

# Memoization Approach
memo = [-1 for _ in range(N+1)]
def fib(n):
    if n <= 2:
        memo[n] = 1

    if memo[n] != -1:
        return memo[n]
    else:
        memo[n] = fib(n-1) + fib(n-2)

    return memo[n]

print(fib(N))

# Tabulation Approach
dp = [0] * (N+1)
dp[1] = 1
dp[2] = 1

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])