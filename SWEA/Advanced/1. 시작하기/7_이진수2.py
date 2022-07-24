T = int(input())
for tc in range(1, T+1):
    N = float(input())
    ans = ""
    while N:
        if N*2 >= 1:
            ans += "1"
            N = (N*2)-1
        else:
            ans += "0"
            N = N*2

        if len(ans) > 13:
            ans = "overflow"
            break

    print("#{} {}".format(tc, ans))