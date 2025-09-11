n = int(input())

# Memoization
memo = [-1] * (n+1)
memo[1] = 0
def step_up(floor):
    if memo[floor] != -1:
        return memo[floor]

    if 1 < floor <= 3:
        memo[floor] = 1

    else:
        memo[floor] = step_up(floor - 2) + step_up(floor - 3)

    return memo[floor]

step_up(n)
print(memo[n] % 10007)

# Tabulation
dp = [0] * 1001
dp[0] = 1
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, n+1):
    dp[i] = (dp[i-2] + dp[i-3]) % 10007

print(dp[n])