# 2562

nums = []

while True:
    try:
        nums.append(int(input()))
    except:
        print(max(nums))
        print(nums.index(max(nums))+1)
        exit()