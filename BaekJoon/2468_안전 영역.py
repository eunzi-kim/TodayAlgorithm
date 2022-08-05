N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0

cnt = 0
max_v = 2
while cnt < max_v:
    visited = [[0]*N for _ in range(N)]

    # 장마철 물에 잠기는 곳 표시
    for i in range(N):
        for j in range(N):
            if board[i][j] > max_v:
                max_v = board[i][j]

            if board[i][j] <= cnt:
                visited[i][j] = 1

    # 안전 영역 탐색
    temp = 0
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                temp += 1
                queue = [(i, j)]
                while queue:
                    v = queue.pop(0)
                    r = v[0]
                    c = v[1]
                    for k in range(4):
                        new_r = r+dr[k]
                        new_c = c+dc[k]
                        if 0 <= new_r < N and 0 <= new_c < N and visited[new_r][new_c] == 0:
                            queue.append((new_r, new_c))
                            visited[new_r][new_c] = 1

    if temp > answer:
        answer = temp

    cnt += 1

print(answer)