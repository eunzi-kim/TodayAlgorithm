N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# M: 세로, N: 가로

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def search():
    cnt = 0
    stack = [(0, 0)]
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    temp = []
    while stack:
        v = stack.pop(0)
        r = v[0]
        c = v[1]
        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]
            if 0 <= new_r < N and 0 <= new_c < M and visited[new_r][new_c] == 0:
                visited[new_r][new_c] = 1
                if board[new_r][new_c] == 0:
                    stack.append((new_r, new_c))
                else:
                    temp.append((new_r, new_c))
                    cnt += 1

    for x, y in temp:
        board[x][y] = 0

    return cnt

time = pre = 0
while True:
    v = search()
    if v:
        time += 1
        pre = v
    else:
        break

print(time)
print(pre)
