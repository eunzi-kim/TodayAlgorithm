T = int(input())

for tc in range(1, T+1):
    N = int(input())
    graph = [0 for _ in range(N+1)]
    
    cnt = 1
    def binary(n):
        global N, cnt
        # 왼쪽 자식 존재
        if n*2 <= N:
            binary(n*2)
        # 채우기
        graph[n] = cnt
        cnt += 1
        # 오른쪽 자식 존재
        if n*2+1 <= N:
            binary(n*2+1)

    binary(1)

    print("#{} {} {}".format(tc, graph[1], graph[N//2]))