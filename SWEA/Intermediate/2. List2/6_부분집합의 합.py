T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    ans = 0

    for i in range(1 << 12):
        cnt = 0
        sum_v = 0
        for j in range(12):
            if i & (1 << j):
                cnt += 1
                sum_v += j+1
        
        if cnt == N and sum_v == K:
            ans += 1

    print("#{} {}".format(tc, ans))