T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))

    oven = [x for x in range(N)]
    i = N
    while len(oven) > 1:
        j = oven.pop(0)
        C[j] = C[j]//2
        if C[j] > 0:
            oven.append(j)
        elif i < M:
            oven.append(i)
            i += 1

    print("#{} {}".format(tc, oven[0]+1))