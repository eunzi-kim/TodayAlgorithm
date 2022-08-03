def solution(s):
    answer = True
    
    stack = []
    for x in s:
        if x == "(":
            stack.append(x)
        else:
            if len(stack):
                stack.pop(-1)
            else:
                answer = False
                break
                
    if len(stack):
        answer = False

    return answer