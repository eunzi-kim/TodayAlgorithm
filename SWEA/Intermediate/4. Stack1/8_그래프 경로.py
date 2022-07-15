T = int(input())
for tc in range(1, T+1):  
    V, E = map(int, input().split())

    Graph = [[] for _ in range(V+1)]

    for _ in range(E):
        s_node, e_node = map(int, input().split())
        Graph[s_node].append(e_node)
    S, G = map(int, input().split())

    ans = 0

    stack = [S]
    while stack:
        v = stack.pop()
        for w in Graph[v]:
            if w == G:
                ans = 1
                break
            else:
                stack.append(w)

    print("#{} {}".format(tc, ans))