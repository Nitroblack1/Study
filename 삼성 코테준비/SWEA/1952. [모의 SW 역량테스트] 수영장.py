T = int(input())
for x in range(1, T + 1):
    day, month, three, year = map(int, input().split())
    usePlan = [0] + list(map(int, input().split()))
    dp = [0] * 13
    
    for i in range(1, 13):
        dp[i] = min(dp[i-1] + usePlan[i] * day, dp[i-1] + month)
        if i >= 3:
            dp[i] = min(dp[i], dp[i-3] + three)
    ans = min(dp[12], year)
    print(f'#{x} {ans}')