K = int(input())

def prime(x):
    if x == 0 or x == 1:
        return False
    else:
        for i in range(2, int(x ** 0.5)+1):
            if x % i == 0:
                return False
            if x % (x // i) == 0:
                return False
    return True

for _ in range(K):
    N = int(input())
    ans = N
    while True:
        if prime(ans):
            break
        else:
            ans += 1

    print(ans)