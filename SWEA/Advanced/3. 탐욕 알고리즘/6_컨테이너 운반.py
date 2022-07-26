T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(reverse=True)
    t.sort(reverse=True)
    
    ans = 0
    i = j = 0
    while i < N and j < M:
        if w[i] <= t[j]:
            ans += w[i]
            i += 1
            j += 1
        else:
            i += 1
    
    print("#{} {}".format(tc, ans))