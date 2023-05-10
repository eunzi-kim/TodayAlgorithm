import heapq

N = int(input())
maze = [list(map(int, input())) for _ in range(N)]

Queue = [(0, 0, 0)]
ans = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [[0]*N for _ in range(N)]
visited[0][0] = 1
while Queue:
    v = heapq.heappop(Queue)
    cnt = v[0]
    r = v[1]
    c = v[2]

    if r == N-1 and c == N-1:
        print(cnt)
        break

    for i in range(4):
        new_r = r+dr[i]
        new_c = c+dc[i]
        if 0 <= new_r < N and 0 <= new_c < N and visited[new_r][new_c] == 0:
            if maze[new_r][new_c]:
                heapq.heappush(Queue, (cnt, new_r, new_c))
            else:
                heapq.heappush(Queue, (cnt+1, new_r, new_c))
            visited[new_r][new_c] = 1
