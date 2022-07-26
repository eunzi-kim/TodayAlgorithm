T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))

    ans = 0
    a = [0]*10
    b = [0]*10


    def run_chk(k, c):
        if 1 < k < 8:
            if c[k-1] and c[k] and c[k+1]:
                return 1
            if c[k] and c[k+1] and c[k+2]:
                return 1
            if c[k-2] and c[k-1] and c[k]:
                return 1
        elif k == 1 or k == 8:
            if c[k-1] and c[k] and c[k+1]:
                return 1
            if k== 1 and c[k] and c[k+1] and c[k+2]:
                return 1
            if k == 8 and c[k-2] and c[k-1] and c[k]:
                return 1
        elif k == 0 and c[k] and c[k+1] and c[k+2]:
            return 1
        elif k == 9 and c[k-2] and c[k-1] and c[k]:
            return 1
        
        return 0            


    for idx in range(0, 12, 2):
        i = card[idx]
        j = card[idx+1]
        a[i] += 1
        b[j] += 1


        if a[i] >= 3:
            ans = 1
            break
        if run_chk(i, a):
            ans = 1
            break

        if b[j] >= 3:
            ans = 2
            break       
        if run_chk(j, b):
            ans = 2
            break

    print("#{} {}".format(tc, ans))