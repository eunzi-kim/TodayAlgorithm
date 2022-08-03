def solution(triangle):
    answer = 0
    for i in range(len(triangle)-1):
        for j in range(i+2):
            if j == 0:
                triangle[i+1][j] += triangle[i][j]
            elif j == i+1:
                triangle[i+1][j] += triangle[i][j-1]
            else:
                if triangle[i][j] > triangle[i][j-1]:
                    triangle[i+1][j] += triangle[i][j]
                else:
                    triangle[i+1][j] += triangle[i][j-1]
        
            if i == len(triangle)-2 and answer < triangle[i+1][j]:
                answer = triangle[i+1][j]
        
    return answer