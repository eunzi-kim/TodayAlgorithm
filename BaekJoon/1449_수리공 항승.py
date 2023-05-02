N, L = map(int, input().split())
pos = list(map(int, input().split()))
pos.sort()

now = pos[0]+L
cnt = 1
for i in range(1, N):
    if pos[i] >= now:
        cnt += 1
        now = pos[i]+L
    
print(cnt)