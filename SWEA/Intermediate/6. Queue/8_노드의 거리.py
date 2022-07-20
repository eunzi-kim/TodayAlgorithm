T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        s, g = map(int, input().split())
        graph[s].append(g)
        graph[g].append(s)
    S, G = map(int, input().split())

    queue = [(S, 0)]
    visited = [0]*(V+1)
    while queue:
        v = queue.pop(0)
        n = v[0]
        d = v[1]+1
        for w in graph[n]:
            if visited[w] >= d or visited[w] == 0:
                visited[w] = d
                visited[w] = d
                queue.append((w, d))

    print("#{} {}".format(tc, visited[G]))