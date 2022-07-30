from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [100000000000]*1000001
    queue = deque()
    queue.append(N)
    visited[N] = 0

    while queue:
        v = queue.popleft()

        a = v+1
        b = v-1
        c = v*2
        d = v-10
        if 0 < a <= 1000000 and visited[a] > visited[v]+1:
            queue.append(a)
            visited[a] = visited[v] + 1
        if 0 < b <= 1000000 and  visited[b] > visited[v]+1:
            queue.append(b)
            visited[b] = visited[v] + 1
        if 0 < c <= 1000000 and  visited[c] > visited[v]+1:
            queue.append(c)
            visited[c] = visited[v] + 1
        if 0 < d <= 1000000 and  visited[d] > visited[v]+1:
            queue.append(d)
            visited[d] = visited[v] + 1
        
    print("#{} {}".format(tc, visited[M]))