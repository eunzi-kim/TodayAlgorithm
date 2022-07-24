T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    Tree = [0 for _ in range(N+1)]

    def chk(x):
        if Tree[x//2] > Tree[x]:
            temp = Tree[x]
            Tree[x] = Tree[x//2]
            Tree[x//2] = temp
            if x//2 > 1:
                chk(x//2)

    for i in range(N):
        Tree[i+1] = arr[i]
        # 부모와 크기 체크
        if i > 0:
            chk(i+1)

    ans = 0
    idx = N//2
    while idx > 0:
        ans += Tree[idx]
        idx //= 2
    print("#{} {}".format(tc, ans))