n, m = map(int, input().split())
ans = 1
for x in range(n, n-m, -1):
    ans *= x
for y in range(1, m+1):
    ans //= y

print(ans)