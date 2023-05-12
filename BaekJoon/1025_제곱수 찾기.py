N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

def checkDouble(x):
    if (x ** 0.5) % 1 == 0:
        return True
    return False

dr = [0]
dc = [0]

for x in range(1, N):
    dr.append(x)
    dr.append(-x)

for y in range(1, M):
    dc.append(y)
    dc.append(-y)

ans = -1
for x in range(N):
    for y in range(M):
        
        for i in range(2*N-1):
            for j in range(2*M-1):

                temp = str(arr[x][y])
                r = x
                c = y
                visitied = [[0] * M for _ in range(N)]
                visitied[r][c] = 1
                if checkDouble(int(temp)) and int(temp) > ans:
                    ans = int(temp)
                while True:
                    r += dr[i]
                    c += dc[j]
                    if 0 <= r < N and 0 <= c < M and visitied[r][c] == 0:
                        temp += str(arr[r][c])
                        visitied[r][c] = 1
                        if checkDouble(int(temp)) and int(temp) > ans:
                            ans = int(temp)
                    else:
                        break

print(ans)