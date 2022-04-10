# 더 맵게

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 최소 힙으로 생성
           
    while scoville[0] < K :
        
        if len(scoville) <= 1 : # (4)제한사항
            return -1
        
        sc1 = heapq.heappop(scoville)
        sc2 = heapq.heappop(scoville)

        newScovile = sc1 + sc2*2

        heapq.heappush(scoville, newScovile)
        answer += 1
            
    return answer
    