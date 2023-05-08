N = int(input())
one = two = 0
one_score = two_score = 0
past_win = 0
for i in range(N):
    T, S = input().split()
    arr = S.split(":")
    time = int(arr[0]) * 60 + int(arr[1])

    if i != 0 and one_score > two_score:
        one += time - past_win
    if i != 0 and one_score < two_score:
        two += time - past_win

    if T == "1":
        one_score += 1
    else:
        two_score += 1

    past_win = time

if one_score > two_score:
    one += 48 * 60 - past_win
if one_score < two_score:
    two += 48 * 60 - past_win

def numToStr(num):
    mm = str(num//60)
    if len(mm) == 1:
        mm = "0" + mm
    ss = str(num%60)
    if len(ss) == 1:
        ss = "0" + ss

    return mm + ":" + ss

print(numToStr(one))
print(numToStr(two))
        