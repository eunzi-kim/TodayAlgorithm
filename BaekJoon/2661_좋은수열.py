N = int(input())

def check(x, m):
    for i in range(1, m//2):
        if x[m-i-1:m+1] == x[m-2*i-2:m-i-1]:
            return False
    return True

visited = [[0, 0, 0] for _ in range(N)]
ans = [""] * N
ans[0] = "1"

i = 1
while i < N:
    for j in range(3):
        k = int(ans[i-1]) - 1
        if int(ans[i-1]) != j+1 and visited[i][j] == 0 and check("".join(ans)+str(j+1), i+1):
            visited[i][j] = 1
            ans[i] = str(j + 1)
            i += 1
            break
    else:
        ans[i-1] = ""
        visited[i] == [0, 0, 0]
        i -= 1

print("".join(ans))