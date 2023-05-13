N, M = map(int, input().split())

arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 0 and arr[i][k] and arr[k][j]:
                arr[i][j] = 1

cnt = 0
for i in range(1, N+1):
    temp_s = 0
    for j in range(1, N+1):
        temp_s += arr[i][j] + arr[j][i]
    if temp_s == N-1:
        cnt += 1

print(cnt)