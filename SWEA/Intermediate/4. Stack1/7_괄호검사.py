T = int(input())
for tc in range(1, T+1):
    input_str = input()

    stack = []
    ans = 0
    for x in input_str:
        if x == "(":
            stack.append(x)
        elif x == "{":
            stack.append(x)
            
        elif x == ")":
            if len(stack):
                v = stack.pop()
                if v != "(":
                    stack.append("(")
                    break
            else:
                stack.append("-1")
                break
        elif x == "}":
            if len(stack):
                v = stack.pop()
                if v != "{":
                    break
            else:
                stack.append("{")
                break
    
    if len(stack) == 0:
        ans = 1

    print("#{} {}".format(tc, ans))