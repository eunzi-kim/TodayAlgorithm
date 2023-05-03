N = int(input())
score = [int(input()) for _ in range(N)]

dp = [0] * (N)
dp[0] = score[0]
if N > 1:
    dp[1] = score[0] + score[1]
if N > 2:
    dp[2] = max(score[0]+score[2], score[1]+score[2])
for i in range(3, N):
    dp[i] = max(score[i]+score[i-1]+dp[i-3], score[i]+dp[i-2])

print(dp[N-1])