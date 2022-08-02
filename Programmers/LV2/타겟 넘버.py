answer = 0

def targetNumber(i, numbers, N):
    global answer
    
    if i == len(numbers):
        if sum(numbers) == N:
            answer += 1

    else:
        targetNumber(i+1, numbers, N)
        numbers[i] = -1 * numbers[i]
        targetNumber(i+1, numbers, N)


def solution(numbers, target):
    targetNumber(0, numbers, target)

    return answer