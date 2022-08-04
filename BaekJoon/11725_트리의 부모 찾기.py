import sys
input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e = map(int, input().split())
    g[s].append(e)
    g[e].append(s)

level = [0]*(n+1)
queue = [1]
while queue:
    w = queue.pop(0)
    for v in g[w]:
        if v != 1 and level[v] == 0:
            queue.append(v)
            level[v] = level[w] + 1

for i in range(2, n+1):
    for x in g[i]:
        if level[i] > level[x]:
            print(x)
            break