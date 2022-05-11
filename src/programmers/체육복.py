'''
체육복
https://programmers.co.kr/learn/courses/30/lessons/42862
'''

# def solution(n, lost, reserve):
#     answer = 0
    
#     student = [True for _ in range(n)]
#     for i in lost:
#         student[i-1] = "lost"
#     for i in reserve:
#         if student[i-1] == "lost":
#             student[i-1] = True
#         else:
#             student[i-1] = "reserve"
        
#     for idx, value in enumerate(student):
#         if value == "lost":
#             if student[idx-1] == "reserve":
#                 student[idx-1] = True
#                 student[idx] = True

#             elif student[idx+1] == "reserve":
#                 student[idx+1] = True
#                 student[idx] = True
#     print(student)
#     return len(student) - student.count("lost")

def solution(n, lost, reserve):
    lost2 = set(lost) - set(reserve)
    reserve2 = set(reserve) - set(lost)
    
    for i in reserve2:
        if i-1 in lost2:
            lost2.remove(i-1)
        elif i+1 in lost2:
            lost2.remove(i+1)
        
    return n - len(lost2)