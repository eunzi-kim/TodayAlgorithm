T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    Al = Bl = 1
    Ar = Br = P

    while True:
        Ac = int((Al+Ar)/2)
        Bc = int((Bl+Br)/2)

        if Ac == A and Bc == B:
            print("#{} 0".format(tc))
            break

        elif Ac == A:
            print("#{} A".format(tc))
            break

        elif Bc == B:
            print("#{} B".format(tc))
            break

        else:
            if Ac < A:
                Al = Ac
            else:
                Ar = Ac

            if Bc < B:
                Bl = Bc
            else:
                Br = Bc