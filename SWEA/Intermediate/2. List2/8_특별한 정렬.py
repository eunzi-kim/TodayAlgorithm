T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    ans = ""
    for i in range(5):
        if i == 4:
            ans += str(arr[N-i-1]) + " " + str(arr[i])
        else:
            ans += str(arr[N-i-1]) + " " + str(arr[i]) + " "

    print("#{} {}".format(tc, ans))