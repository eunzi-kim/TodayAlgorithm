import itertools

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    ans = 10*N

    arr = [x for x in range(N)]
    for perm in itertools.permutations(arr, N):
        sum_v = 0
        for i in range(N):
            sum_v += board[i][perm[i]]
            # 가지치기
            if sum_v >= ans:
                break
        if ans > sum_v:
            ans = sum_v

    print("#{} {}".format(tc, ans))