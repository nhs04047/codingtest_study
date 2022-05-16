'''
N으로 표현
https://programmers.co.kr/learn/courses/30/lessons/42895
'''

def solution(N, number):
    
    if N == number:
        return 1
    
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N)*(i)))
        
    for i in range(2, 9):
        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i-j]:
                    dp[i].add(num1+num2)
                    dp[i].add(num1-num2)
                    dp[i].add(num2-num1)
                    dp[i].add(num1*num2)
                    if num2 != 0 :
                        dp[i].add(num1//num2)
                    if num1 != 0 :
                        dp[i].add(num2//num1)
        if number in dp[i] :
            return i
    return -1

    
    # for i in range(1, 8):
    #     for j in dp[i-1]:
    #         dp[i].add(j+N)
    #         dp[i].add(j-N)
    #         dp[i].add(N-j)
    #         dp[i].add(j*N)
    #         if N != 0:
    #             dp[i].add(j//N)
    #         if j != 0:
    #             dp[i].add(N//j)
    #         dp[i].add(int(str(N)*(i+1)))
    