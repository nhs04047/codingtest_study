# 1427-소트인사이드

def sorting(arr):
    if len(arr) <= 1:
        return arr
    
    length = len(arr) - 1
    for i in range(length):
        for j in range(length-i):
            if arr[j] < arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr

nums = list(map(int, input()))

print("".join(map(str, sorting(nums))))


