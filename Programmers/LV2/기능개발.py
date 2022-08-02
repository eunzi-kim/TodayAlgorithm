def solution(progresses, speeds):
    answer = []
    
    while progresses:
        if progresses[0] < 100:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
        else:
            temp = 0
            while progresses:
                if progresses[0] >= 100:
                    progresses.pop(0)
                    speeds.pop(0)
                    temp += 1
                else:
                    break
            answer.append(temp)
            
    return answer