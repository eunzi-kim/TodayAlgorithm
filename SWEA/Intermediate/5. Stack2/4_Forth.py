T = int(input())

for tc in range(1, T+1):
    arr = list(input().split(" "))
    
    stack = []
    for x in arr:
        if x == "+":
            if len(stack) < 2:
                print("#{} {}".format(tc, "error"))
                break
            v2 = stack.pop()
            v1 = stack.pop()
            stack.append(v1+v2)
        elif x == "*":
            if len(stack) < 2:
                print("#{} {}".format(tc, "error"))
                break
            v2 = stack.pop()
            v1 = stack.pop()
            stack.append(v1*v2)
        elif x == "-":
            if len(stack) < 2:
                print("#{} {}".format(tc, "error"))
                break
            v2 = stack.pop()
            v1 = stack.pop()
            stack.append(v1-v2)
        elif x == "/":
            if len(stack) < 2:
                print("#{} {}".format(tc, "error"))
                break
            v2 = stack.pop()
            v1 = stack.pop()
            stack.append(v1//v2)
        elif x == ".":
            if len(stack) != 1:
                print("#{} {}".format(tc, "error"))
                break
            print("#{} {}".format(tc, stack.pop()))
        else:
            stack.append(int(x))