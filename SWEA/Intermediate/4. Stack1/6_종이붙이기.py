T = int(input())

def paper_attach(n):
    if n == 1:
        return 1
    elif n == 2: 
        return 3
    else:
        return paper_attach(n-1) + 2*paper_attach(n-2)

for tc in range(1, T+1):
    N = int(input())
    ans = paper_attach(N//10)

    print("#{} {}".format(tc, ans))