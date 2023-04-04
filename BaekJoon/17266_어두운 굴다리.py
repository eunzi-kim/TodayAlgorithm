N = int(input())
M = int(input())
x = list(map(int, input().split()))

h = 1

while True:
    pos = 0
    for lamp in x:
        if lamp - h > pos:
            break
        else:
            pos = lamp + h
    
    if pos >= N:
        break
    
    h += 1
    
print(h)