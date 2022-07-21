T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    arr = list(map(int, input().split()))
    for x in range(M-1):
        i = 0
        data = list(map(int, input().split()))
        while i < (x+1)*N:
            if arr[i] > data[0]:
                break
            else:
                i += 1
        if i < (x+1)*N:
            arr[i:i] = data
        else:
            arr = arr + data

    ans = ""
    if N*M > 10:
        for j in range(N*M-1, N*M-11, -1):
            ans += " " + str(arr[j])
    else:
        for j in range(N*M-1, -1, -1):
            ans += " " + str(arr[j])
    print("#{} {}".format(tc, ans[1:]))