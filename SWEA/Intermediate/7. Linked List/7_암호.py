T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))

    i = 0
    for k in range(K):
        i += M
        if i > N+k:
            i %= (N+k)
        if i == N+k:
            arr.append(arr[i-1]+arr[0])
        else:
            arr[i:i] = [arr[i-1] + arr[i]]

    ans = ""
    if len(arr) > 10:
        for j in range(len(arr)-1, len(arr)-11, -1):
            ans += " " + str(arr[j])
    else:
        for j in range(len(arr)-1, -1, -1):
            ans += " " + str(arr[j])
    print("#{} {}".format(tc, ans[1:]))