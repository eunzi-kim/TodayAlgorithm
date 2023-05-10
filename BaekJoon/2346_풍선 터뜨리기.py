N = int(input())
arr = list(map(int, input().split()))

visited = [0] * N
visited[0] = 1
i = 0
ans = [1]
while len(ans) <  N:
    visited[i] = 1
    v = arr[i]
    cnt = 0
    if v > 0:
        while cnt < v:
            if visited[i] == 0:
                cnt += 1
            i += 1
            if i == N:
                i = 0
        i -= 1
    else:
        while cnt < -v:
            if visited[i] == 0:
                cnt += 1
            if i == -1:
                i = N-1
            i -= 1
        i += 1
    
    i %= N

    visited[i] = 1
    ans.append(i+1)

print(*ans)