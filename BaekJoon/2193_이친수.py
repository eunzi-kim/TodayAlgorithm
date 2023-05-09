import sys
input = sys.stdin.readline

N = int(input())

zero = [0] * N
one = [0] * N
one[0] += 1

if N > 1:
    zero[1] += 1
    for i in range(2, N):
        zero[i] += one[i-1] + zero[i-1]
        one[i] += zero[i-1]

print(zero[N-1] + one[N-1])