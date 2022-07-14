T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    chk = False
    ans = ""

    for i in range(N):
        for j in range(N-M+1):
            r_ans = ""
            c_ans = ""

            # 행 회문 체크
            for k in range(M//2):
                if board[i][j+k] == board[i][j+M-k-1]:
                    r_ans += board[i][j+k]
                else:
                    break
            else:
                chk = True
                if M%2:
                    ans = r_ans + board[i][j+M//2] + r_ans[-1::-1]
                else:
                    ans = r_ans + r_ans[-1::-1]

            # 열 회문 체크
            for k in range(M//2):
                if board[j+k][i] == board[j+M-k-1][i]:
                    c_ans += board[j+k][i]
                else:
                    break
            else:
                chk = True
                if M%2:
                    ans = c_ans + board[j+M//2][i] + c_ans[-1::-1]
                else:
                    ans = c_ans + c_ans[-1::-1]

        if chk:
            break           
            
    print("#{} {}".format(tc, ans))