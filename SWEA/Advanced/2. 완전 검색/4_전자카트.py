import itertools

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    ans = 1000000000000000

    arr = [x for x in range(1, N)]
    for w in itertools.permutations(arr, N-1):
        temp = 0
        pre = 0
        for i in w:
            temp += board[pre][i]
            pre = i
        temp += board[pre][0]
        
        if temp < ans:
            ans = temp

    print("#{} {}".format(tc, ans))