name = input()

arr = [0]*26
for x in name:
    i = ord(x) - 65
    arr[i] += 1

ans = ""
cnt = 0
temp = ''

def attachStr(k, n):
    temp_str = ""
    for _ in range(n//2):
        temp_str += chr(k+65)
    return temp_str

for i in range(26):
    if arr[i] % 2:
        cnt += 1
        if cnt == 1:
            temp = chr(i+65)
            ans += attachStr(i, arr[i])
        else:
            ans = "I'm Sorry Hansoo"
            break
    else:
        ans += attachStr(i, arr[i])

if cnt == 0:
    ans += ans[::-1]
elif cnt == 1:
    ans += temp + ans[::-1]

print(ans)