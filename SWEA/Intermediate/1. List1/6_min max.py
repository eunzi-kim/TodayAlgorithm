T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_v = arr[0]
    min_v = arr[0]

    for x in arr:
        if x > max_v:
            max_v = x
        if x < min_v:
            min_v = x

    print("#{} {}".format(tc, max_v-min_v))