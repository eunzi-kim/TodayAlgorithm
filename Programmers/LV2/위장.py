def solution(clothes):
    answer = 1
    info = []
    num = []
    
    for cloth in clothes:
        if cloth[1] not in info:
            info.append(cloth[1])
            num.append(1)
        else:
            i = info.index(cloth[1])
            num[i] += 1
            
    for n in num:
        answer *= (n+1)
    
    return answer-1