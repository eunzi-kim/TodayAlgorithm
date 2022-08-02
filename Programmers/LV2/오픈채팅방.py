def solution(record):
    answer = []
    
    info = {}
    
    for alert in record:
        v = alert.split(" ")
        if v[0] != "Leave":
            info[v[1]] = v[2]
            
    for alert in record:
        v = alert.split(" ")
        if v[0] == "Enter":
            answer.append(info[v[1]] + "님이 들어왔습니다.")
        elif v[0] == "Leave":
            answer.append(info[v[1]] + "님이 나갔습니다.")
    
    return answer