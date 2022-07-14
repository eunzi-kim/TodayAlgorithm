T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    N = len(str1)
    cnt_list = [0] * N

    max_v = 0

    for i in range(N):
        for x in str2:
            if str1[i] == x:
                cnt_list[i] += 1
                if max_v < cnt_list[i]:
                    max_v = cnt_list[i]

    print("#{} {}".format(tc, max_v))