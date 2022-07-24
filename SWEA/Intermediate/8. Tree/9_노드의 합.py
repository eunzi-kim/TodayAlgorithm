T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    Tree = [0] * (N+1)
    for _ in range(M):
        idx, n = map(int, input().split())
        Tree[idx] = n

    for i in range(N, 0, -1):
        Tree[i//2] += Tree[i]

    print("#{} {}".format(tc, Tree[L]))