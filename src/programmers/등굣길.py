'''
등굣길
https://programmers.co.kr/learn/courses/30/lessons/42898
'''

# def solution(m, n, puddles):

#     path = [[0]*m for _ in range(n)]
#     for i in range(len(path)):
#         for j in range(len(path[i])):
#             if i==0 and j==0:
#                 path[i][j] = 1
#             elif [j+1, i+1] in puddles:
#                 path[i+1][j+1] = 0
#             elif i == 0:
#                 path[i][j] = path[i][j-1]
#             elif j == 0:
#                 path[i][j] = path[i-1][j]
#             else:
#                 path[i][j] = path[i][j-1] + path[i-1][j]

#     return path[n-1][m-1]%1000000007

def solution(m, n, puddles):

    path = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i==1 and j==1:
                path[i][j] = 1
            elif [j, i] in puddles:
                path[i][j] = 0
            else :
                path[i][j] = path[i-1][j]+path[i][j-1]

    return path[n][m]%1000000007

print(solution(4, 3, [[2,2]]))