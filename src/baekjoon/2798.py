# 2798 블랙잭

def brackJack(N, M, nums):
    maxSum = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):            
                if nums[i]+nums[j]+nums[k] > M :
                    continue
                else:
                    maxSum = max(maxSum, nums[i]+nums[j]+nums[k])
    return maxSum

N, M = map(int, input().split())
nums = list(map(int, input().split()))

print(brackJack(N, M, nums))
            