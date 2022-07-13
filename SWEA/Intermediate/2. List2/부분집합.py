N = int(input())

for i in range(1 << N):
    sub_set = []
    for j in range(N):
        if i & (1 << j):
            sub_set.append(j)
    
    print(sub_set)