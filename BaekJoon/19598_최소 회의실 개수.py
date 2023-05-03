import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()

room = []
for i in range(N):
    s, e = arr[i]

    if i == 0:
        room.append(e)
    else:
        for j in range(len(room)):
            if room[j] <= s:
                room[j] = e
                break
        else:
            room.append(e)

print(len(room))