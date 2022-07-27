def quick(left, right):
    if left == right:
        return arr

    pivot = left
    i = left + 1
    j = right - 1

    while i <= j:
        while i <= j and arr[pivot] >= arr[i]:
            i += 1
        while i <= j and arr[pivot] <= arr[j]:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[pivot] = arr[pivot], arr[j]    
    quick(left, j)
    quick(j+1, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick(0, N)
    print("#{} {}".format(tc, arr[N//2]))