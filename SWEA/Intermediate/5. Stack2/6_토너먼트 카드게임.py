T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split(" ")))

    # 가위, 바위, 보 게임 함수
    def game(i, j):
        if card[i] == card[j]:
            return i
        elif card[i] == 1:
            if card[j] == 2:
                return j
            elif card[j] == 3:
                return i
        elif card[i] == 2:
            if card[j] == 1:
                return i
            elif card[j] == 3:
                return j
        elif card[i] == 3:
            if card[j] == 1:
                return j
            elif card[j] == 2:
                return i

    stack = [i for i in range(N)]

    # 그룹 나누기
    def group(arr):
        if len(arr) == 2:
            temp.append(game(arr[0], arr[1])) 
        elif len(arr) == 1:
            temp.append(arr[0])
        else:
            group(arr[:(len(arr)+1)//2])
            group(arr[(len(arr)+1)//2:])

    # 1명이 남을 때까지 진행
    while len(stack) > 1:
        temp = []
        group(stack)
        stack = temp

    print("#{} {}".format(tc, stack[0]+1))