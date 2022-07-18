T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    ans = 0

    # 1. 출발점 탐색
    stack = []
    for r in range(N):
        for c in range(N):
            if board[r][c] == 2:
                stack.append((r, c))
                visited[r][c] = 1
                break

    if len(stack) == 0:
        ans == "error"

    # 2. 미로 찾기
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    while stack:
        v = stack.pop()
        r = v[0]
        c = v[1]
        
        if board[r][c] == 3:
            ans = 1
            break

        for i in range(4):
            new_r = r+dr[i]
            new_c = c+dc[i]
            if 0 <= new_r < N and 0 <= new_c < N and board[new_r][new_c] != 1 and visited[new_r][new_c] == 0:
                visited[new_r][new_c] = 1
                stack.append((new_r, new_c))

    print("#{} {}".format(tc, ans))