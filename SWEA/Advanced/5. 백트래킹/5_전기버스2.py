T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split())) + [0]
    N = arr[0]

    board = [N]*(N+1)
    board[1] = 0

    queue = [(1, arr[1])]
    while queue:
        w = queue.pop(0)
        x = w[0]
        v = w[1]

        for i in range(1, v+1):
            j = x+i
            if j > N:
                j = N-1
            if board[x]+1 < board[j]:
                board[j] = board[x]+1
                queue.append((j, arr[j]))

    print("#{} {}".format(tc, board[N]-1))