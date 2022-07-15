T = int(input())
for tc in range(1, T+1):

    stack = []
    
    for x in input():
        if len(stack) and stack[-1] == x:
            stack.pop()
        else:
            stack.append(x)

    print("#{} {}".format(tc, len(stack)))