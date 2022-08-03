def solution(N, road, K):
    dis = [[100000000]*(N+1) for _ in range(N+1)]
    g = [[] for _ in range(N+1)] 

    for w in road:
        s = w[0]
        e = w[1]
        d = w[2]
        g[s].append(e)
        g[e].append(s)
        if dis[s][e] > d:
            dis[s][e] = d
        if dis[e][s] > d:
            dis[e][s] = d
        
    queue = g[1]
    while queue:
        x = queue.pop(0)
        for i in g[x]:
            if i != 1 and dis[1][i] >= dis[1][x] + dis[x][i]:
                dis[1][i] = dis[1][x] + dis[x][i]
                queue.append(i)

    answer = 1
    for v in dis[1]:
        if v <= K:
            answer += 1
    
    return answer