T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 10000000000000000000000
    visited = [0]*N

    def perm(idx, sum_v):
        global ans
        if idx == N:
            if ans > sum_v:
                ans = sum_v
                return
        if sum_v >= ans:
            return
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                perm(idx+1, sum_v+board[idx][i])
                visited[i] = 0        

    perm(0, 0)

    print("#{} {}".format(tc, ans))