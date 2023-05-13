import sys
input = sys.stdin.readline

N = int(input())
C_W = list(map(int, input().split()))
M = int(input())
B_W = list(map(int, input().split()))

visited = [0] *  M

C_W.sort()
B_W.sort()

now = [M-1]*N

cnt = 0
while True:
    if B_W[-1] > C_W[-1]:
        cnt = -1
        break

    cnt += 1
    for i in range(N):
        j = now[i]

        while B_W[j] > C_W[i] or visited[j]: 
            j -= 1
            if j < 0:
                break
        
        if j >= 0 and B_W[j] <= C_W[i] and visited[j] == 0:
            now[i] = j - 1
            visited[j] = 1

    if now[-1] < 0 or min(visited) == 1:
        break

print(cnt)