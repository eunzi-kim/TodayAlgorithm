def solution(numbers):
    answer = ''
    n = len(numbers)
    for i in range(n):
        numbers[i] = str(numbers[i]) * 3
    numbers.sort(reverse=True)
    for number in numbers:
        answer += number[:len(number)//3]
    return str(int(answer))