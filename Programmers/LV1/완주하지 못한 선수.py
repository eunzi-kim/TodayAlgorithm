def solution(participant, completion):
    participant.sort()
    completion.sort()
    n = len(completion)
    i = 0
    while i < n:
        if participant[i] == completion[i]:
            i += 1
        else:
            return participant[i]
    return participant[n]