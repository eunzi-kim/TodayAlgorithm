T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    zzang = [x for x in range(N)]


    def find(x):
        if x != zzang[x]:
            zzang[x] = find(zzang[x])
            return zzang[x]
        else:
            return zzang[x]


    def union(a, b):
        head_a = find(a)
        head_b = find(b)
        if head_a > head_b:
            zzang[head_a] = head_b
        else:
            zzang[head_b] = head_a


    for i in range(0, M):
        union(arr[2*i]-1, arr[2*i+1]-1)

    head = []
    for z in zzang:
        v = find(z)
        if v not in head:
            head.append(v)

    print("#{} {}".format(tc, len(head)))