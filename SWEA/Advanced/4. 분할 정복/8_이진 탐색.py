T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()

    def find(x):
        chk = 0
        l = 0
        r = N-1
        while l <= r:
            m = (l+r)//2
            if x == A[m]:
                return True
            elif x < A[m]:
                r = m-1
                if chk == 1:
                    return False
                chk = 1
            else:
                l = m+1
                if chk == 2:
                    return False
                chk = 2
        return False

    ans = 0
    for j in range(M):
        if find(B[j]):
            ans += 1

    print("#{} {}".format(tc, ans))