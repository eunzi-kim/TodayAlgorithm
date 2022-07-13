T = int(input())
for tc in range(1, T+1):
    N = int(input())

    m = [[0]*10 for _ in range(10)]
    cnt = 0

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                m[r][c] += color
                if m[r][c] == 3:
                    cnt += 1
                    
    print("#{} {}".format(tc, cnt))