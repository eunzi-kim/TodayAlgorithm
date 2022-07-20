T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Maze = [list(map(int, input())) for _ in range(N)]
    visited = [[N*N+N]*N for _ in range(N)]

    ans = 1

    for r in range(N):
        for c in range(N):
            if Maze[r][c] == 2:
                Queue = [(r, c)]
                visited[r][c] = 0
                break

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while Queue:
        v = Queue.pop(0)
        r = v[0]
        c = v[1]

        if Maze[r][c] == 3:
            ans = visited[r][c]

        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]
            if 0 <= new_r < N and 0 <= new_c < N and Maze[new_r][new_c] != 1 and visited[new_r][new_c] > visited[r][c]:
                Queue.append((new_r, new_c))
                visited[new_r][new_c] = visited[r][c] + 1

    print("#{} {}".format(tc, ans-1))
