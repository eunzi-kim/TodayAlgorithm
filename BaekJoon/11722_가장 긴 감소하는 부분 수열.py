N = int(input())
A = list(map(int, input().split()))

dp = [0]*(N+1)
answer = 0

for i in range(N-1):
    for j in range(i+1, N):
        if A[i] > A[j]:
            dp[j] = max(dp[i] + 1, dp[j])
            if answer < dp[j]:
                answer =dp[j]

print(answer+1)
