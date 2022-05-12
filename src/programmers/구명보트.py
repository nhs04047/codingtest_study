'''
구명보트
https://programmers.co.kr/learn/courses/30/lessons/42885
'''

# def solution(people, limit):
#     answer = 0
#     boat = []
    
#     while people:
#         maxWeight = 0
#         maxIdx = 0
        
#         if 2 > len(people):
#             answer += 1
#             break
            
#         boat.append(people.pop())
#         for idx, value in enumerate(people):
#             boat.append(value)
#             print(sum(boat))
#             if limit >= sum(boat) and maxWeight < sum(boat):
#                 maxIdx = idx
#                 maxWeight = sum(boat)
#             boat.pop()
#         if maxIdx != 0:
#             del people[maxIdx]
#         boat.pop()
#         answer += 1            
    
#     return answer

def solution(people, limit):
    people.sort()
    answer = 0
    
    i = 0
    j = len(people)-1
    while i <= j:
        answer+=1
        if people[i] + people[j] <= limit:
            i+=1
        j-=1
            
    return answer