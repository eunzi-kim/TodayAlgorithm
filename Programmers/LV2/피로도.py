import itertools

def solution(k, dungeons):
    answer = 0
    
    n = len(dungeons)
    arr = [x for x in range(n)]
    
    for w in itertools.permutations(arr, n):
        tired = k
        temp = 0
        for i in w:
            v = dungeons[i]
            if v[0] <= tired:
                tired -= v[1]
                temp += 1
                
        if temp > answer:
            answer = temp
            
    return answer