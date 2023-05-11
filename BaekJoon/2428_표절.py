import sys
input = sys.stdin.readline

N = int(input())
F = list(map(int, input().split()))
F.sort()

def search(x):
    start = x+1
    end = N-1
    mid = 0
    re = x
    while start <= end:
        mid = (start + end) // 2
        if F[x] >= F[mid]*0.9:
            start = mid + 1
            re = mid
        else:
            end = mid - 1
    
    return re - x

cnt = 0
for i in range(N-1):
    cnt += search(i)

print(cnt)
