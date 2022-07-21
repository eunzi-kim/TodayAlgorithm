T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M):
        info = list(input().split())
        i = int(info[1])
        if info[0] == "I":            
            arr[i:i] = [int(info[2])]
        elif info[0] == "D":
            arr.pop(i)
        else:
            arr[i] = int(info[2])

    if len(arr) <= L:
        print("#{} {}".format(tc, -1))
    else:
        print("#{} {}".format(tc, arr[L]))