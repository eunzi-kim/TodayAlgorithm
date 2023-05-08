T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    num_info = [i for i in range(N)]

    cnt = 0
    while arr:
        x = arr.pop(0)
        y = num_info.pop(0)
        if arr and max(arr) > x:
            arr.append(x)
            num_info.append(y)
        else:
            cnt += 1
            if y == M:
                break

    print(cnt)