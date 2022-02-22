# 2750 - 수 정렬하기

def sorting(arr):
    if len(arr) <= 1:
        return arr
    
    length = len(arr) - 1
    for i in range(length):
        for j in range(length-i):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr

N = int(input())
nums = []

for i in range(N):
    nums.append(int(input()))

for i in sorting(nums):
    print(i)
