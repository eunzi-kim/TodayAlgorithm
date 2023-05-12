N = int(input())
arr = [0]

def check(v):
    if v < 10:
        return True
    w = str(v)
    pre = 10
    for i in range(len(w)):
        if int(w[i]) < pre:
            pre = int(w[i])
        else:
            temp = str(int(w[0:i]) + 1) + "0" * (len(w)-i)
            return int(temp)
    return 1

for i in range(N):
    x = arr[-1]
    while True:
        x += 1

        val = check(x)
        if val == 1:
            arr.append(x)
            break
        else:
            x = val - 1
    
        if x > 9876543210:
            break
    
    if x > 9876543210:
        break

if len(arr) <= N:
    print(-1)
else:
    print(arr[N])
