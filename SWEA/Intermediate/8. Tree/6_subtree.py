T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    child = [[] for _ in range(E+2)]
    for i in range(0, len(arr), 2):
        child[arr[i]].append(arr[i+1])
    stack = [N]
    ans = 0
    while stack:
        v = stack.pop(-1)
        ans += 1
        for w in child[v]:
            stack.append(w)
    print("#{} {}".format(tc, ans))
