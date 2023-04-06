N = int(input())
score = []
for _ in range(N):
    score.append(int(input()))

now = score[-1]
ans = 0
for i in range(N-2, -1, -1):
    if score[i] >= now:
        ans += score[i] - now + 1
        score[i] = now - 1
    now = score[i]

print(ans)