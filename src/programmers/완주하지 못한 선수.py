# 완주하지 못한 선수

def solution(participant, completion):
    answer = ''
#
#       sort와 for문
      
    # participant.sort()
    # completion.sort()
    
    # for i in range(len(participant)):
    #     if participant[i] != completion[i]:
    #         answer = participant[i]
    #         return answer

#       hash

    hashSum = 0
    nameDict = {}
    
    for name in participant:
        nameDict[hash(name)] = name
        hashSum += int(hash(name))
        
    for name in completion:
        hashSum -= int(hash(name))
        
    answer = nameDict[hashSum]
    return answer

print(solution(["mislav", "stanko", "mislav", "ana"],
                ["stanko", "ana", "mislav"]))