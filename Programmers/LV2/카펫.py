def solution(brown, yellow):
    answer = []
    
    yellow_cd = []
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0:
            yellow_cd.append((i, yellow//i))
    
    for w in yellow_cd:
        x = w[0]
        y = w[1]
        if brown == x*2 + y*2 + 4:
            answer = [y+2, x+2]
    
    return answer