def merge(L):
    M = len(L)
    if M <= 1:
        return L
    else:
        l = merge(L[0:M//2])
        r = merge(L[M//2:M])
        return merge_sort(l, r)


def merge_sort(left, right):
    global cnt

    if left[-1] > right[-1]:
        cnt += 1

    L = len(left)
    R = len(right)
    i = j = 0
    temp = []
    while i < L or j < R:
        if i < L and j < R:
            if left[i] <= right[j]:
                temp.append(left[i])
                i += 1
            else:
                temp.append(right[j])
                j += 1
        elif i == L:
            temp.append(right[j])
            j += 1
        else:
            temp.append(left[i])
            i += 1
    return temp


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    ans = merge(arr)[N//2]

    print("#{} {} {}".format(tc, ans, cnt))