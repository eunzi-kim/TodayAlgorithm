T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    gas = list(map(int, input().split()))
    
    cnt = 0
    pos = N
    charge = N

    while True:
        pos -= K

        if pos <= 0:
            break

        for x in range(pos, charge):
            if x in gas:
                pos = x
                charge = x
                cnt += 1
                break
        else:
            cnt = 0
            break
    
    print("#{} {}".format(tc, cnt))