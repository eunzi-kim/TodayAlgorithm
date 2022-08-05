import sys
input = sys.stdin.readline

N, M = map(int, input().split())

child = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
cnt = [1] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    child[A].append(B)
    indegree[B] += 1

# 선수과목이 없는 과목 탐색
queue = []
for i in range(N+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    v = queue.pop(0)
    for x in child[v]:
        cnt[x] = cnt[v] + 1
        indegree[x] -= 1

        if indegree[x] == 0:
            queue.append(x)

print(*cnt[1:])
