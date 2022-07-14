def solution(nums):
    numsSet = set(nums)
    if len(numsSet) > len(nums)/2:
        return len(nums)/2
    return len(numsSet)