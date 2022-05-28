'''
로또의 최고 순위와 최저 순위
https://programmers.co.kr/learn/courses/30/lessons/77484
'''

def solution(lottos, win_nums):
    rankList = [6, 6, 5, 4, 3, 2, 1]
    cnt = 0
    
    for i in lottos : 
        if i in win_nums :
            cnt += 1 
    
    rankHigh = rankList[cnt + lottos.count(0)]
    rankLow = rankList[cnt]
    
    answer = [rankHigh, rankLow]

    return answer