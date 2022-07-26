T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = [[1000000]*N for _ in range(N)]

    dr = [1, 0]
    dc = [0, 1]
    queue = [(0, 0)]
    ans[0][0] = board[0][0]
    while queue:
        v = queue.pop(0)
        r = v[0]
        c = v[1]

        for i in range(2):
            new_r = r+dr[i]
            new_c = c+dc[i]
            if 0 <= new_r < N and 0 <= new_c < N and board[new_r][new_c] + ans[r][c] < ans[new_r][new_c]:
                queue.append((new_r, new_c))
                ans[new_r][new_c] = board[new_r][new_c] + ans[r][c] 

    print("#{} {}".format(tc, ans[N-1][N-1]))