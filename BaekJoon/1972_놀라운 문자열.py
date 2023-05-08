while True:
    x = input()
    if x == "*":
        break
    n = len(x)
    ans = x + " is surprising."
    for i in range(n):
        arr = []
        for j in range(n-i-1):
            temp = x[j] + x[i+j+1]
            if temp not in arr:
                arr.append(temp)
            else:
                ans = x + " is NOT surprising."
                break

        if ans == x + " is NOT surprising.":
            break
    print(ans)