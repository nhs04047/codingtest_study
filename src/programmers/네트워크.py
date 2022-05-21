'''
네트워크
https://programmers.co.kr/learn/courses/30/lessons/43162
'''

def dfs(num, visited, computers):
    visited[num] = True
    
    for idx, net in enumerate(computers[num]):
        if net == 1 and (not visited[idx]):
            dfs(idx, visited, computers)

def solution(n, computers):
    visited = [False]*n
    answer = 0 
    
    for num in range(n):
        if not visited[num]:
            dfs(num, visited, computers)
            answer += 1
            
    return answer