# 소수 만들기

from itertools import combinations


def isPrimNum(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, (num//2)+1):
            if num % i == 0:
                return False
        return True


def solution(nums):

    answer = 0

    com = list(combinations(nums, 3))
    for i in com:
        if isPrimNum(sum(i)) == True:
            answer += 1
    return answer
