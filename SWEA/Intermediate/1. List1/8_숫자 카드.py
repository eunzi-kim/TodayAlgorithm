T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    card = [0]*10
    max_v = 0
    max_i = 10

    for i in range(N):
        card[arr[i]] += 1
        if card[arr[i]] > max_v:
            max_v = card[arr[i]]
            max_i = arr[i]
        elif card[arr[i]] == max_v:
            if max_i < arr[i]:
                max_i = arr[i]

    print("#{} {} {}".format(tc, max_i, max_v))