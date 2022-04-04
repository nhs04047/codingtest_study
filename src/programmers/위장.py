from functools import reduce

def solution(clothes):
    answer = 0
    
    clothesTable = {}
    
    for i in clothes :     
        if i[1] in clothesTable:
            clothesTable[i[1]] += 1
        else:
            clothesTable[i[1]] = 1

    # reduce(집계 함수, 순회 가능한 데이터[, 초기값])
    answer = reduce(lambda x, y: x*(y+1), clothesTable.values(), 1) - 1
            
    return answer