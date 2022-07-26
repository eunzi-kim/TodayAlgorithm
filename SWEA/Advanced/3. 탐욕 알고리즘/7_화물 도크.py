T = int(input())
for tc in range(1, T+1):
    N = int(input())
    info = []
    for _ in range(N):
        s, e = map(int, input().split())
        info.append([e-s, s, e])
    
    time = [0]*25
    ans = 0

    info.sort()
    for v in info:
        s = v[1]
        e = v[2]
        for i in range(s, e):
            if time[i]:
                break
            else:
                time[i] += 1
        else:
            ans += 1
    
    print("#{} {}".format(tc, ans))