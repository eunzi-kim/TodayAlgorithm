N, K = map(int, input().split())

arr = [x for x in range(N+1)]
visited = [0] * (N+1)
cnt = ans = 0

for i in range(2, N+1):
    for j in range(i, N+1, i):
        if visited[j] == 0:
            visited[j] = 1
            cnt += 1
            if cnt == K:
                ans = j
                break
    if ans:
        break

print(ans)