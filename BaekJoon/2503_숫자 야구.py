from itertools import permutations

N = int(input())
arr = list(permutations([1,2,3,4,5,6,7,8,9], 3))

for _ in range(N):
    info = list(map(int, input().split()))
    score = list(str(info[0]))
    remove_cnt = 0

    for i in range(len(arr)):
        i -= remove_cnt
        s_cnt = b_cnt = 0
        for j in range(3):
            score[j] = int(score[j])
            if score[j] in arr[i]:
                if score[j] == arr[i][j]:
                    s_cnt += 1
                else:
                    b_cnt += 1

        if s_cnt != info[1] or b_cnt != info[2]:
            arr.pop(i)
            remove_cnt += 1

print(len(arr))

