N = int(input())

dp = [0] * (N+1)
dp[1] = 0
for x in range(2, N+1):
    dp[x] = dp[x-1] + 1
    if x % 3 == 0:
        dp[x] = min(dp[x//3]+1, dp[x])
    if x % 2 == 0:
        dp[x] = min(dp[x//2]+1, dp[x])
        
print(dp[N])