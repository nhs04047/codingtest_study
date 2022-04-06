# 기능개발

import math

def solution(progresses, speeds):
    answer = []
    
    left = []

    for progress, speed in zip(progresses, speeds):
        left.append(math.ceil((100-progress)/speed))

    while left:
        leftNow = left.pop(0)
        done = 1
        while len(left) != 0 and leftNow >= left[0] :
            done += 1
            left.pop(0)
            
        answer.append(done)
            
        print(answer)
    return answer