def solution(bridge_length, weight, truck_weights):
    answer = 0
    i = 0
    queue = []
    time = []
    while i == 0 or queue:
        answer += 1
        for j in range(len(time)):
            time[j] += 1
        
        if time and time[0] >= bridge_length:
            queue.pop(0)
            time.pop(0)
            
        if i < len(truck_weights):
            if sum(queue) + truck_weights[i] <= weight and len(queue) < bridge_length:
                queue.append(truck_weights[i])
                time.append(0)
                i += 1

    return answer