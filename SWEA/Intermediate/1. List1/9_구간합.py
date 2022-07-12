T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    max_s = 0
    min_s = 100000*50

    for i in range(N-M+1):
        temp_s = 0
        for j in range(i, i+M):
            temp_s += arr[j]
        if temp_s > max_s:
            max_s = temp_s
        if temp_s < min_s:
            min_s = temp_s

    print("#{} {}".format(tc, max_s-min_s))