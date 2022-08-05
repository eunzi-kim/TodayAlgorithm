S = input()
K = input()

real_s = ''
for x in S:
    if x.isnumeric() == 0:
        real_s += x

if K in real_s:
    print(1)
else:
    print(0)