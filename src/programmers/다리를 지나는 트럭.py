# 다리를 지나는 트럭

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridgeSum = 0
    
    bridge = [0] * bridge_length
    bridgeQ = deque(bridge)
    truck = deque(truck_weights)

    while bridgeQ :
      answer += 1
      bridgeSum -= bridgeQ.popleft()

      if truck:
        if bridgeSum + truck[0] <= weight:
          bridgeSum += truck[0]
          bridgeQ.append(truck.popleft())
        else:
          bridgeQ.append(0)

              
    return answer

  
print(solution(2,10,[7,4,5,6]))

# 테스트 케이스 5번을 통과하지 못 했었지만, 만복할 때 마다 sum 연산을 해주는 것은 많은 리소스를 먹는 다는 것을 알고 수정 후 테스트 케이스 통과